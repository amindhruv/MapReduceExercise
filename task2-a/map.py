#!/usr/bin/python

import sys

for line in sys.stdin:
 if not line.strip():
  continue
 line = line.strip()
 key, value = line.split("\t",1)
 vlist=value.split(",")
 if float(vlist[11]) <= 4 and float(vlist[11]) >=0:
  print "0,4\t1"
 if float(vlist[11]) <= 8 and float(vlist[11]) >=4.01:
  print "4.01,8\t1"
 if float(vlist[11]) <= 12 and float(vlist[11]) >=8.01:
  print "8.01,12\t1"
 if float(vlist[11]) <= 16 and float(vlist[11]) >=12.01:
  print "12.01,16\t1"
 if float(vlist[11]) <= 20 and float(vlist[11]) >=16.01:
  print "16.01,20\t1"
 if float(vlist[11]) <= 24 and float(vlist[11]) >=20.01:
  print "20.01,24\t1"
 if float(vlist[11]) <= 28 and float(vlist[11]) >=24.01:
  print "24.01,28\t1"
 if float(vlist[11]) <= 32 and float(vlist[11]) >=28.01:
  print "28.01,32\t1"
 if float(vlist[11]) <= 36 and float(vlist[11]) >=32.01:
  print "32.01,36\t1"
 if float(vlist[11]) <= 40 and float(vlist[11]) >=36.01:
  print "36.01,40\t1"
 if float(vlist[11]) <= 44 and float(vlist[11]) >=40.01:
  print "40.01,44\t1"
 if float(vlist[11]) <= 48 and float(vlist[11]) >=44.01:
  print "44.01,48\t1"
 if float(vlist[11]) >= 48.01:
  print "48.01,infinite\t1"