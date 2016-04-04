#!/usr/bin/python

import sys
import string
import random
import p7_fastExp

def fermat( n, k ):
	i = 0
	if n < 4:
		return True
	while i < k:
		a = 2 + random.randint(1, n-2)
		if p7_fastExp.fastExp(a, n-1, n) != 1:
			return False
		i += 1
	return True
	
if len(sys.argv) > 2:
	print fermat(int(sys.argv[1]), int(sys.argv[2]))
else:
	print 'SYNOPSIS: ./p3 number1 number2'

