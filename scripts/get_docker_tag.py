#!/usr/bin/env python

import os
import sys

tag = 1 

tag_file = '/opt/docker/tag/' + sys.argv[1]

if os.path.exists(tag_file):
    f = open(tag_file) 
    t = f.read().strip()
    if t:
        tag = int(t) + 1
    f.close()

f = open(tag_file, 'w+') 
tag = str(tag)
f.write(tag)
f.close()

print(tag)
