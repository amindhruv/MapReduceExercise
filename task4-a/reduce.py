#!/usr/bin/python

import sys
prevKey=""
key=""
ctr=0
rev=0
tip=0

for line in sys.stdin:
 prevKey=key
 line = line.strip()
 key, value = line.split("\t",1)
 valuelist=value.split(",")
 
 if(prevKey==""):
  prevKey=key

 if(prevKey==key):
  ctr=ctr+1 
  rev=rev+float(valuelist[0])
  tip=tip+float(valuelist[1])

 if(prevKey!=key):
  print "%s\t%d,%.2f,%.2f" % (prevKey,ctr,rev,(tip/ctr))
  ctr=1 
  rev=float(valuelist[0])
  tip=float(valuelist[1])

print "%s\t%d,%.2f,%.2f" % (key,ctr,rev,(tip/ctr))