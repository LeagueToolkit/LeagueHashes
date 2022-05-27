#!/bin/env python3
import sys
import json
from xxhash import xxh64_intdigest

MASK = 0xFF_FF_FF_FF_FF
MASK2 = MASK >> 4

def xxh40(s, mask = MASK):
    return xxh64_intdigest(s.lower()) & mask

def read_hash_dict(listname):
    with open(listname) as inf:
        result = {
            int(line.strip().split(' ')[0], 16) & MASK : \
                ' '.join(line.strip().split(' ')[1:]) \
                    for line in inf.readlines() \
                        if line.strip()
        }
        for k, v in result.items():
            assert(k & MASK2 == xxh40(v, MASK2))
        return result

def merge(dst, src):
    for h, v in src.items():
        if h in dst:
            assert(v.lower() == dst[h].lower())
        else:
            dst[h] = v
    dst_list_sorted = list((k, v) for k,v in dst.items())
    dst_list_sorted.sort(key = lambda x: (x[1], x[0]))
    dst_list_stringified = list(f"{k:010x} {v}" for k,v in dst_list_sorted)
    return "\n".join(dst_list_stringified)

dst_filename = sys.argv[1]
src_filename = sys.argv[2]

dst = read_hash_dict(dst_filename)
src = read_hash_dict(src_filename)

merged = merge(dst, src)
with open(dst_filename, 'w') as outf:
    outf.write(merged)
