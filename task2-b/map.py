#!/usr/bin/python

import sys

for line in sys.stdin:
 line = line.strip()
 key, value = line.split("\t",1)
 valuelist=value.split(",")
 
 if (float(valuelist[16])) <= 10:
  print "%s\t%s" % ("a",valuelist[0]) 