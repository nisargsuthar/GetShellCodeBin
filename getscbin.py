#!/usr/bin/python
import os
import sys
import re

if os.path.isfile(sys.argv[1]):
    sc = open(sys.argv[1]).read()
else:
    sc = sys.argv[1]

bin_sc = re.sub('%u(..)(..)', lambda x: chr(
    int(x.group(2), 16))+chr(int(x.group(1), 16)), sc)

try:
    FILE = open("shellcode.bin", "wb")
    FILE.write(bin_sc)
    FILE.close()
except Exception, e:
    print 'Cannot save binary to disk: %s' % e
