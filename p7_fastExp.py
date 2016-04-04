#!/usr/bin/python

import sys
import string
import random

#		a^b mod m
def fastExp(a, b, m):
	result = 1
	x = a % m
	i = 1
	while i <= b:
		x %= m
		if b & i != 0:
			result *= x
			result %= m
		x *= x
		i +=2
	return result % m

