#!/usr/bin/python

import sys
import string
import p8
import p1

def cryptRSA(msg, e, n):
	return (msg ** e) % n

def decryptRSA(enc, d, n):
	return (enc ** d) % n
	
if len(sys.argv) > 1:
	text = readFile(sys.argv[1])
	print text
	numbers = txtToNum(text)
	prettyNumbers = ''
	for x in numbers:
		prettyNumbers += str(x) + ' '
	print prettyNumbers
	
	e, d, n = p8.generateKeys()
	crypted = []
	prettyCrypt = ''
	for x in numbers:
		c = cryptRSA(x, e, n)
		crypted.append(c)
		prettyCrypt += str(c) + ' '
	print prettyCrypt
	print p1.numToTxt(prettyCrypt)
	
   # decrypted = []
	#for x in crypted:
	#	decrypted.append(decryptRSA(x, d, n))
	#print decrypted
	
else:
	print 'SYNOPSIS: ./p9 file'
