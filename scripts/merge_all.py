#!/bin/env python3
import sys
import json

def read_hash_set(listname):
    with open(listname) as inf:
        return { 
            int(line, 16) for line in inf.readlines() if line
        }

def read_hash_set_json(jsonname):
    with open(jsonname) as inf:
        return set(json.load(inf))

def merge(dst, src):
    dst_list_sorted = list(dst | src)
    dst_list_sorted.sort()
    dst_list_stringified = list(f"{x:08x}" for x in dst_list_sorted)
    return "\n".join(dst_list_stringified)

dst_filename = sys.argv[1]
src_filename = sys.argv[2]

dst = read_hash_set_json(dst_filename) if dst_filename.endswith(".json") else read_hash_set(dst_filename)
src = read_hash_set_json(src_filename) if src_filename.endswith(".json") else read_hash_set(src_filename)

merged = merge(dst, src)
with open(dst_filename, 'w') as outf:
    outf.write(merged)
