#!/bin/env python3
import sys
import json
import os
import glob

dst_filename = sys.argv[1]
src_filename = sys.argv[2]

def process_all_meta_types(sourcename):
    results = set()
    for filename in glob.iglob(sourcename, recursive=True):
        with open(filename) as inf:
            j = json.load(inf)
            for h in j['classes'].keys():
                results.add(int(h, 16))
    results = list(results)
    results.sort()
    return "\n".join([f"{x:08x}" for x in results]) + '\n'

dst_filename = sys.argv[1]
src_filename = sys.argv[2]

merged = process_all_meta_types(src_filename)
with open(dst_filename, 'w') as outf:
    outf.write(merged)
