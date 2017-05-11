#!/usr/bin/python

import sys

for line in sys.stdin:
 line = line.strip()
 key, value = line.split("\t",1)
 keylist=key.split(",")
 keydate, keytime=keylist[3].split(" ",1)
 valuelist=value.split(",")
 
 tempTotal=float(valuelist[11])+float(valuelist[12])+float(valuelist[14])
 print "%s\t%f,%f" % (keydate,tempTotal,float(valuelist[15])) 