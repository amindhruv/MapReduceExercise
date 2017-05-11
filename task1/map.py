#!/usr/bin/python

import sys
import os

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	if "medallion" not in line:
		try:
			file_name = os.environ['mapreduce_map_input_file']
		except KeyError:
			file_name = os.environ['map_input_file']
		if not line.strip():
			continue
		line = line.strip()
		line = line.split(",")
		if "fare" in file_name :
			print "%s,%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s" % (line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
		if "trip" in file_name :
			print "%s,%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (line[0],line[1],line[2],line[5],line[3],line[4],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13])