#!/usr/bin/python

import sys
import string
import p8
import p1

def cryptRSA(msg, e, n):
	return = (msg ** e) % n

def decryptRSA(enc, d, n):
	return (enc ** d) % n
	
if len(sys.argv) > 1:
	e, d, n = generateKeys()
	text = readFile(sys.argv[1])
	print text
	numbers = txtToNum(text)
	
	prettyNumbers = ''
	for x in numbers:
		x = cryptRSA(x, e, n)
		
	print prettyNumbers
	
	prettyNumbers = ''
	for x in numbers:
		x = decryptRSA(x, d, n)
		prettyNumbers += str(x) + ' '
	print numToTxt(prettyNumbers)
	
else:
	print 'SYNOPSIS: ./p9 file'
