import sys
import string
import p4_euklides

def relativelyPrime(l1, l2):
	if p4_euklides.nwd( l1, l2 ) == 1:
		return True
	else:
		return False
	
if len(sys.argv) > 2:
	l1 = int(sys.argv[1])
	l2 = int(sys.argv[2])
	if relativelyPrime(l1, l2):
		print 'Numbers', l1, "and", l2, 'are relatively prime'
	else:
		print 'Numbers', l1, 'and', l2, 'aren\'t relatively prime'
else:
	print 'SYNOPSIS: ./p5 number1 number2'

