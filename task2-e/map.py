#!/usr/bin/python

import sys
import os

for line in sys.stdin:
 if not line.strip():
  continue
 line = line.strip()
 key, value = line.split("\t",1)
 keylist=key.split(",")
# keydate, keytime=keylist[3].split(" ",1)
 
 print "%s,%s\t%s" % (keylist[0],keylist[3],"1")