#!/usr/bin/env python

import sys
import os

for line in sys.stdin:

    key, value = line.strip().split('\t')

    medallion = key.split(',')[0]
    license = key.split(',')[1]

    print ("%s\t%s" % (license, medallion))
