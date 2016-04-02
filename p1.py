#!/usr/bin/python

import random
import sys
import hashlib
import string

def readFile(path):
	return open(path).read()

def writeFile(text, path):
	open(path, 'w').write(text)

def txtToNum(text):
	tab = []
	if len(text) % 2 != 0:
		text += ' '
	i = 0
	while i < len(text):
		tab.append(ord(text[i]) * 1000 + ord(text[i+1]))
		i += 2
	return tab
	
def numToTxt(text):
	result = ''
	tab = text.split()
	for x in tab:
		x = int(x)
		result += chr(x // 1000)
		result += chr(x % 1000)
	return result
	
if len(sys.argv) > 1:
	print txtToNum(readFile(sys.argv[1]))
	
else:
	print 'SYNOPSIS: ./p4 file [file2] [...]'
	print 'SYNOPSIS: ./p4 -c file'


