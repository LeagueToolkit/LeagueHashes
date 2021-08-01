#!/bin/env python3
import sys
import json

def fnv1a(s):
    h = 0x811c9dc5
    for b in s.encode('ascii').lower():
        h = ((h ^ b) * 0x01000193) & 0xFF_FF_FF_FF
    return h

def read_hash_dict(listname):
    with open(listname) as inf:
        result = {
            int(line[:8], 16) : line[9:].rstrip() for line in inf.readlines() if line.rstrip()
        }
        for k, v in result.items():
            assert(k == fnv1a(v))
        return result

def merge(dst, src):
    for h, v in src.items():
        if h in dst:
            assert(v.lower() == dst[h].lower())
        else:
            dst[h] = v
    dst_list_sorted = list((k, v) for k,v in dst.items())
    dst_list_sorted.sort(key = lambda x: (x[1], x[0]))
    dst_list_stringified = list(f"{k:08x} {v}" for k,v in dst_list_sorted)
    return "\n".join(dst_list_stringified)

dst_filename = sys.argv[1]
src_filename = sys.argv[2]

dst = read_hash_dict(dst_filename)
src = read_hash_dict(src_filename)

merged = merge(dst, src)
with open(dst_filename, 'w') as outf:
    outf.write(merged)
