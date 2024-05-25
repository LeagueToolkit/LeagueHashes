#!/bin/env python
import json
import sys
import os
import re
import glob

# A python class with mandatory () for base classes
RE_CLASS = re.compile(r'^class\s+(\w+)\s*\(((?:\s*\w+\s*,?\s*)*)\):$')
# A python field with mandatory () for flattened typedef
RE_FIELD = re.compile(r'^    (\w+)\s*:\s*\(((?:\s*\w+\s*,?\s*)*)\)$')

def rehex_fnv1a(s):
    if s.startswith('0x'): return hex(int(s, 16))
    h = 0x811c9dc5
    for b in s.encode('ascii').lower():
        h = ((h ^ b) * 0x01000193) % 0x100000000
    return hex(h)

def read_hashes(filename):
    with open(filename, "r") as inf:
        lines = [ x.rstrip().split(' ') for x in inf.readlines() ]
        return { hex(int(h, 16)) : v for h, v in lines }

def read_database(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as inf:
        db = {}
        fields = None
        for line in inf.readlines():
            line = line.rstrip()
            if line.lstrip() == "pass":
                continue
            if not line or line.lstrip().startswith('#'):
                continue
            if m := RE_CLASS.match(line):
                kname = rehex_fnv1a(m.group(1))
                bases = set(rehex_fnv1a(b.strip()) for b in m.group(2).split(',') if b.strip())
                fields = set()
                if kname in db: raise ValueError(f"Duplicate class: {line}")
                db[kname] = { 'bases': bases, 'fields': fields }
                continue
            if m := RE_FIELD.match(line):
                fname = rehex_fnv1a(m.group(1))
                ft, kt, vt, kh = tuple(t.strip() for t in m.group(2).split(','))
                field = (fname, (ft, kt, vt, rehex_fnv1a(kh)))
                if fields == None: raise ValueError(f"Stray field: {line}")
                if field in fields: raise ValueError(f"Duplicate field: {line}")
                fields.add(field)
                continue
            raise ValueError(f"Failed to parse: {line}")
        return db

def write_databse(filename, db):
    def h2type(h):
        return h if not h in h_types else h_types[h]
    def h2field(h):
        return h if not h in h_fields else h_fields[h]
    with open(filename, 'w') as outf:
        outf.write("#!python\n")
        for kname in sorted(db.keys()):
            klass = db[kname]
            outf.write(f"class {h2type(kname)}({', '.join(h2type(b) for b in sorted(klass['bases']))}):\n")
            for fname, (ft, kt, vt, kh) in sorted(klass['fields']):
                outf.write(f"    {h2field(fname)}: ({ft}, {kt}, {vt}, {h2type(kh)})\n")
            outf.write(f"    pass\n")
            outf.write('\n')

def import_database(db, meta):
    for kname, klass in meta['classes'].items():
        kname = rehex_fnv1a(kname)
        if not kname in db: db[kname] = { 'bases': set(), 'fields': set() }
        bases = db[kname]['bases']
        fields = db[kname]['fields']
        if klass["base"]: bases.add(rehex_fnv1a(klass["base"]))
        for base in klass["secondary_bases"].keys(): bases.add(rehex_fnv1a(base))
        for fname, field in klass["properties"].items():
            if field['container'] and field['map']: raise ValueError("container/map conflict!")
            ftype = [ field['value_type'] ]
            if field['container']:
                ftype.append(hex(field['container']['fixed_size'] or 0))
                ftype.append(field['container']['value_type'])
            elif field['map']:
                ftype.append(field['map']['key_type'])
                ftype.append(field['map']['value_type'])
            else:
                ftype.append(hex(0))
                ftype.append(hex(0))
            if field['other_class']:
                ftype.append(rehex_fnv1a(field['other_class']))
            else:
                ftype.append(hex(0))
            fields.add((rehex_fnv1a(fname), tuple(ftype)))

def read_meta(filename):
    def convert_type(t, is_old):
        if t == None: return None
        if is_old:
            if t >= 18 and t < 0x80: t = (t - 18) | 0x80
            if t >= 0x81: t += 1
        if t == 1: return "Bool"
        if t == 2: return "I8"
        if t == 3: return "U8"
        if t == 4: return "I16"
        if t == 5: return "U16"
        if t == 6: return "I32"
        if t == 7: return "U32"
        if t == 8: return "I64"
        if t == 9: return "U64"
        if t == 10: return "F32"
        if t == 11: return "Vec2"
        if t == 12: return "Vec3"
        if t == 13: return "Vec4"
        if t == 14: return "Mtx44"
        if t == 15: return "Color"
        if t == 16: return "String"
        if t == 17: return "Hash"
        if t == 18: return "File"
        if t == 0x80 | 0: return "List"
        if t == 0x80 | 1: return "List2"
        if t == 0x80 | 2: return "Pointer"
        if t == 0x80 | 3: return "Embed"
        if t == 0x80 | 4: return "Link"
        if t == 0x80 | 5: return "Option"
        if t == 0x80 | 6: return "Map"
        if t == 0x80 | 7: return "Flag"
        raise ValueError(f"Unknown old type: {hex(t)}")
    def convert_hex(h):
        if not h: return None
        return hex(h)
    def convert_digit(h):
        if not h: return None
        return int(h)
    def convert_container_storage(s, f):
        if f: return "Fixed"
        return None
    def convert_map_storage(s):
        if s == 0: return "StdMap"
        if s == 1: return "StdUnorderedMap"
        return None
    with open(filename) as inf:
        meta = json.load(inf)
        # No upgrade necessary
        if isinstance(meta["classes"], dict):
            return meta
        # Very old meta, type indexes need fixup
        is_old = tuple(int(x) for x in meta["version"].split('.')) < (10, 8)
        # Convert to new json format somehwat
        return {
            "classes": {
                hex(klass["hash"]) : {
                    "alignment": klass["alignment"],
                    "base": convert_hex(klass["parentClass"]),
                    "defaults": None,
                    "fn": {
                        "constructor": convert_hex(klass["constructor"]),
                        "destructor": convert_hex(klass["destructor"]),
                        "inplace_constructor": convert_hex(klass["inplaceconstructor"]),
                        "inplace_destructor": convert_hex(klass["inplacedestructor"]),
                        "register": convert_hex(klass["initfunction"]),
                        "upcast_secondary": convert_hex(klass["upcastSecondary"]),
                    },
                    "is": {
                        "interface": klass["isInterface"],
                        "property_base": klass["isPropertyBase"],
                        "secondary_base": klass["isSecondaryBase"],
                        "unk5": False if not "isUnk5" in klass else klass["isUnk5"],
                        "value": klass["isValue"],
                    },
                    "properties": {
                        hex(prop["hash"]): {
                            "bitmask": prop["bitmask"],
                            "container": None if not prop["containerI"] else {
                                "fixed_size": convert_digit(prop["containerI"]["fixedSize"]),
                                "storage": convert_map_storage(prop["containerI"]["fixedSize"]),
                                "value_size": prop["containerI"]["elemSize"],
                                "value_type": convert_type(prop["containerI"]["type"], is_old),
                                "vtable": convert_hex(prop["containerI"]["vtable"]),
                            },
                            "map": None if not prop["mapI"] else {
                                "key_type": convert_type(prop["mapI"]["key"], is_old),
                                "storage": convert_map_storage(prop["mapI"]["storage"]),
                                "value_type": convert_type(prop["mapI"]["value"], is_old),
                                "vtable": convert_hex(prop["mapI"]["vtable"]),
                            },
                            "offset": prop["offset"],
                            "other_class": convert_hex(prop["otherClass"]),
                            "value_type": convert_type(prop["type"], is_old),
                        } for prop in klass["properties"]
                    },
                    "secondary_bases": {
                        convert_hex(bhash): boffset for bhash, boffset in klass["secondaryBases"]
                    },
                    "secondary_children": {
                        convert_hex(chash): coffset for chash, coffset in klass["secondaryChildren"]
                    },
                    "size": klass["classSize"]
                } for klass in meta["classes"]
            }
        }

if __name__ == '__main__':
    h_fields = read_hashes(f"hashes/hashes.binfields.txt")
    h_types = read_hashes(f"hashes/hashes.bintypes.txt")
    database = read_database(sys.argv[1])
    for arg in sys.argv[2:]:
        for filename in glob.iglob(arg):
            meta = read_meta(filename)
            import_database(database, meta)
    write_databse(sys.argv[1], database)
