#!/usr/bin/env python

import time
from datetime import date
import random


size = 630611
outfile = open("randomSeq.tfa", "w")
outfile.write(">KM RANDOM SEQ: " + str(time.time()) + "\n")

counter = 0
for i in range(size):
    base = random.randint(0,100)
    if (0 <= base < 20):
	outfile.write("A")
    elif (20 <= base < 55):
	outfile.write("C")
    elif (55 <= base < 85):
	outfile.write("G")
    elif (85 <= base < 100):
	outfile.write("T")
    elif (100 <= base <= 100):
	outfile.write("T")
    counter +=1
    if (counter > 99):
	outfile.write("\n")
	counter = 0
