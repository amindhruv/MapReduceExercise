#!/usr/bin/python
import sys

for line in sys.stdin:
 line = line.strip()
 key, value = line.split("\t",1)
 valuelist=value.split(",")
 
 print "%s\t%s" % (valuelist[3],"0") 