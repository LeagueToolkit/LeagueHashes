#!/bin/env python3
import sys
import json
import os
import glob

def split_line(line, skip = 0):
    # Start from hash part
    start = skip
    # Skip any leading prefixes
    while start < len(line) and line[start].islower() or line[start] == '_':
        start += 1
    # Set end to next character
    end = start + 1
    while end < len(line):
        # If we hit start of next word yield
        if line[end].isupper():
            yield line[start:end]
            start = end
        end += 1
    # If there is any uyieled data, yield it now
    if end != start and start < len(line):
        yield line[start:end]

def process_file(inf, seen):
    for line in inf.readlines():
        line = line.rstrip()
        if not line:
            continue
        if ' ' in line:
            line = line[9:]
        for x in split_line(line):
            if not x in seen:
                seen.add(x)
                print(x)

seen = set()
for arg in sys.argv[1:]:
    if arg == '-':
        process_file(sys.stdin, seen)
        continue
    for filename in glob.iglob(arg, recursive=True):
        with open(filename) as inf:
            process_file(inf, seen)
