#!/usr/bin/python

import random
import sys
import hashlib
import string

def readFile(path):
	return open(path).read()

def writeFile(text, path):
	open(path, 'w').write(text)

def lenght():
	return 2

def txtToNum(text):
	tab = []

	con = len(text) % lenght()
	if con != 0:
		for x in range(0,con):
			text += ' '
	i = 0
	while i < len(text):
		tmp =''
		for x in range(i,lenght()+i):
			tmp += str(ord(text[x]))
		tab.append(long(tmp))
		i += lenght()
	return tab
	
def numToTxt(text):
	result = ''
	tab = text.split()
	for x in tab:
		result += chr(x // 1000)
		result += chr(x % 1000)
	return result

def numToString(numbers):
	prettyNumbers = ''
	for x in numbers:
		prettyNumbers += str(x) + ' '
	return prettyNumbers	
	
if len(sys.argv) > 1:
	text = readFile(sys.argv[1])
	print text
	numbers = txtToNum(text)
	prettyNumbers = numToString(numbers)
	print prettyNumbers
	print numToTxt(prettyNumbers)
	
else:
	print 'SYNOPSIS: ./p1 file'



