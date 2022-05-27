#!/bin/env python3
import sys
import json
from xxhash import xxh64_intdigest

MASK = 0xF_FF_FF_FF_FF

def xxh36(s):
    return xxh64_intdigest(s.lower()) & MASK

def read_hash_dict(listname):
    with open(listname) as inf:
        result = {
            int(line.strip().split(' ')[0], 16) & MASK : \
                ' '.join(line.strip().split(' ')[1:]) \
                    for line in inf.readlines() \
                        if line.strip()
        }
        for k, v in result.items():
            assert(k == xxh36(v))
        return result

def merge(dst, src):
    for h, v in src.items():
        if h in dst:
            assert(v.lower() == dst[h].lower())
        else:
            dst[h] = v
    dst_list_sorted = list((k, v) for k,v in dst.items())
    dst_list_sorted.sort(key = lambda x: (x[1], x[0]))
    dst_list_stringified = list(f"{k:09x} {v}" for k,v in dst_list_sorted)
    return "\n".join(dst_list_stringified)

dst_filename = sys.argv[1]
src_filename = sys.argv[2]

dst = read_hash_dict(dst_filename)
src = read_hash_dict(src_filename)

merged = merge(dst, src)
with open(dst_filename, 'w') as outf:
    outf.write(merged)
