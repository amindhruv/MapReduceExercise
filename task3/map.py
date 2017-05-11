#!/usr/bin/python

import sys

for line in sys.stdin:
 line = line.strip()
 
 if (len(line.split("\t")) == 2):
  splits = line.split("\t")
  keysplit=splits[0].split(",")
  print "%s\t%s,%s,%s" % (keysplit[0],"0",",".join(keysplit[1:]),splits[1])
 else :
  splits = line.split(",",1)
  print "%s\t%s,%s" % (splits[0],"1",".".join(splits[1:]))