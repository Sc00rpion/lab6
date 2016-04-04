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
	e, d, n = p8.generateKeys()
	text = p1.readFile(sys.argv[1])
	print text
	numbers = p1.txtToNum(text)
    crypted = []
	for x in numbers:
		crypted.append(cryptRSA(x, e, n))
	print crypted
    decrypted = []
	for x in crypted:
		decrypted.append(decryptRSA(x, d, n))
	print decrypted
	
else:
	print 'SYNOPSIS: ./p9 file'
