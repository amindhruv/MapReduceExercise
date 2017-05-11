#!/usr/bin/python
import sys
curr_key=None
sum=0

for line in sys.stdin:
 key,count=line.strip().split("\t",1)
 try:
  count=int(count)
 except ValueError:
  continue
 if key==curr_key:
  sum+=count
 else:
  if curr_key:
   print "%s\t%d" %(curr_key,sum)
  curr_key=key
  sum=count
print "%s\t%d" %(curr_key,sum)