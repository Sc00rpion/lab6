#!/usr/bin/python

import sys
import string
def modularInverse(a, b):
	x, u, w, z = 0, 1, a, b
	q = 0
	while w:
		if w < z:
			u, x = x, u
			w, z = z, w
		q = w // z
		u = u - q * x
		w = w - q * z
	if z != 1:
		print "no solution"
		return 0
	if x < 0:
		x += b
	return x

if len(sys.argv) > 2:
	l_1 = int(sys.argv[1])
	l_2 = int(sys.argv[2])
	#28 i 75 ma byc 67
	print modularInverse(l_1, l_2)
else:
	print 'SYNOPSIS: ./p6 number1 number2'
