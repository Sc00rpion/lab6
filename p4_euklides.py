#!/usr/bin/python
import sys
import string
def nwd(a, b):
	while b:
		a, b = b, a%b
	return a
			
print nwd(int(sys.argv[1]), int(sys.argv[2]))
