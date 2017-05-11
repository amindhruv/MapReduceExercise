#!/usr/bin/python

import sys

for line in sys.stdin:
 valuelist=[]
 ctr=0
 line = line.strip()
 key, value = line.split("\t",1)
 while(ctr<20):
  valuelist=value.partition(",")
  #print "%s" % (value)
  value=valuelist[2]
  if(ctr==17):
   tip=valuelist[0]
  elif(ctr==14):
   rev=valuelist[0]
  elif(ctr==15):
   sur=valuelist[0]
  
  ctr=ctr+1

 value=value.split(",")
 for valu in value :
  if(valu=="WAV" or valu=="HYB" or valu=="CNG" or valu=="LV1" or valu=="DSE" or valu=="NRML"):
   key=valu
 
 if((float(rev)+float(sur)+float(tip))==0):
  print "%s\t%f,%f" % (key,(float(rev)+float(sur)+float(tip)),0) 
 else:
  print "%s\t%f,%f" % (key,float(rev)+float(sur)+float(tip),float(tip)/(float(rev)+float(sur)+float(tip))*100)