#!/bin/env python3
import sys
import json
import os
import glob

dst_filename = sys.argv[1]
src_filename = sys.argv[2]


def process_all_meta_fields(sourcename, results):
    for filename in glob.iglob(sourcename, recursive=True):
        with open(filename) as inf:
            j = json.load(inf)
            for k in j['classes'].values():
                for h in k['properties'].keys():
                    results.add(int(h, 16))
    results = list(results)
    results.sort()
    return "\n".join([f"{x:08x}" for x in results]) + '\n'

dst_filename = sys.argv[1]
src_filename = sys.argv[2]

results = set()
with open(dst_filename, 'r') as inf:
    for line in inf.readlines():
        line = line.strip()
        if not line:
            continue
        results.add(int(line, 16))

merged = process_all_meta_fields(src_filename, results)
with open(dst_filename, 'w') as outf:
    outf.write(merged)
