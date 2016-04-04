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
	numbers = txtToNum(text)
	e, d, n = p8.generateKeys()
	crypted = []
	decrypted = []
	for x in numbers:
		singleCrypt = cryptRSA(x, e, n)
		singleDecrypt = decryptRSA(singleCrypt, d, n)
		crypted.append(singleCrypt)
		decrypted.append(singleDecrypt)
	
	print text
	print p1.numToString(numbers)
	print p1.numToString(crypted)
	print p1.numToTxt(decrypted)

else:
	print 'SYNOPSIS: ./p9 file'
