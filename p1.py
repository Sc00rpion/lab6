#!/usr/bin/python

import random
import sys
import hashlib
import string

def readFile(path):
	return open(path).read()

def writeFile(text, path):
	open(path, 'w').write(text)

def numCharTogether():
	return 3

def numComplement():
	return 4

def complement0(x):
	l = len(x)
	if l != numComplement():
		tmp = ''
		for i in range(numComplement() - l):
			tmp += '0'
		return tmp + x
	else:
		return x
		
def addSpace(text, number):
	for x in range(0, number):
		text += ' '
	return text
		
def txtToNum(text):
	tab = []
	con = len(text) % numCharTogether()
	text = addSpace(text, con)
	i = 0
	while i < len(text):
		tmp =''
		for x in range(i,numCharTogether()+i):
			tmp += complement0(str(ord(text[x])))
		tab.append(tmp)
		i += numCharTogether()
	return tab
	
def numToTxt(text):
	result = ''
	tab = text.split()
	for x in tab:
		i = 0
		while i < len(x):
			result += chr(int(x[i:numComplement() + i]))
			i += numComplement()
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



