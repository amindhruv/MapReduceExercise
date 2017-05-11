#!/usr/bin/python
import sys
curr_medallions=None
days=None
date_count=0
trip_count=0

for line in sys.stdin:
 
 tDetais,count=line.strip().split("\t",1)
 medallion,date=tDetais.strip().split(",",1)
 try:
  count=int(count)
 except ValueError:
  continue
 
 if medallion==curr_medallions:
  if days!=date:
   date_count+=1
   days=date
  trip_count+=1
 else:
  if curr_medallions:
   print "%s\t%d,%.2f" %(curr_medallions,trip_count,trip_count/float(date_count))
  curr_medallions=medallion
  days=date
  date_count=1
  trip_count=count

print "%s\t%d,%.2f" %(curr_medallions,trip_count,trip_count/float(date_count))