#!/usr/bin/python
import sys
key=""
prevKey=""
ctr=0

for line in sys.stdin:
 
 prevKey=key
 line = line.strip()
 key, value = line.split("\t",1)
 
 if(prevKey==""):
  prevKey=key
 
 ctr=ctr+1
 
 if(key!=prevKey):
  ctr=ctr-1
  print "%s\t%s" % (prevKey,ctr)
  ctr=1

print "%s\t%s" % (key,ctr)