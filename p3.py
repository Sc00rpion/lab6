import sys
import string
import random
def fastExp(a, b, m):
	result = 1
	x = a % m
	i = 1
	while i <=b:
		x %= m
		if b & i != 0:
			result *= x
			result %= m
		x *= x
		i +=2
	return result % m

def Fermat( n, k ):
	i = 0
	if n < 4:
		return True
	while i < k:
		a = 2 + random.randint(1, n-2)
		if fastExp(a, n-1, n) != 1:
			return False
		i += 1
	return True

print Fermat(int(sys.argv[1]), int(sys.argv[2]))
