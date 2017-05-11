#!/usr/bin/python

import sys
key=""
prevKey=""
totalRev=0
totalToll=0

for line in sys.stdin:
 
 prevKey=key
 line = line.strip()
 key, value = line.split("\t",1)
 valuelist = value.split(",")
 rev=float(valuelist[0])
 toll=float(valuelist[1])

 if(prevKey==""):
  prevKey=key
 
 if(key==prevKey):
  totalRev=totalRev+rev
  totalToll=totalToll+toll

 if(key!=prevKey):
  print "%s\t%.2f,%.2f" % (prevKey,totalRev,totalToll)
  totalRev=rev
  totalToll=toll

print "%s\t%.2f,%.2f" % (key,totalRev,totalToll)