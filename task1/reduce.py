#!/usr/bin/python

import sys

current_key = ''
fares = []
trips = []

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	key,value = line.strip().split("\t",1)
	value_list = value.strip().split(",")
	
	if key == current_key:
		if len(value_list) == 10 :
			trips += [value]
		else:
			fares += [value]
		
	else:
		if current_key and trips and fares:
			for i in trips:
				for j in fares:
					print '%s\t%s,%s'%(current_key,i,j)
		current_key = key
		if len(value_list) == 10 :
			trips = [value]
			fares = []
		else:
			fares = [value]
			trips = []
			
if current_key and trips and fares:
    for i in trips:
        for j in fares:
            print '%s\t%s,%s'%(current_key,i,j)