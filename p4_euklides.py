#!/usr/bin/python
import sys
import string
def nwd(a, b):
	while b:
		a, b = b, a%b
	return a
	
if len(sys.argv) > 2:
	print nwd(int(sys.argv[1]), int(sys.argv[2]))
else:
	print 'SYNOPSIS: ./p5 number1 number2'			

