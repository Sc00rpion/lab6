#!/usr/bin/python

import random
import sys
import hashlib
import string

def txtToNum(filePath):
	tab = []
	inFile = open(filePath).read()
	if len(inFile) % 2 != 0:
		inFile.append(' ')
	for i in range(0,len(inFile)):
		tab.append(ord(inFile[i]) * 1000 + ord(inFile[i+1]))
	return tab
	
if len(sys.argv) > 1:
	
else:
	print 'SYNOPSIS: ./p4 file [file2] [...]'
	print 'SYNOPSIS: ./p4 -c file'


