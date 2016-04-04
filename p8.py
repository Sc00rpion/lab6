#!/usr/bin/python

import sys
import string
import random
import p7_fastExp
import p5
import p3
import p4_euklides
import p6

def randomPQ():
	r=random.randint(550,1000)
	while p3.fermat(r, r) == False:
		r=random.randint(550,1000)
	return r
	
def randomE(p,q):
	e = random.randint(550,1000)
	pq = (p-1)*(q-1)
	while p5.relativelyPrime(e, pq) != True:
		e=random.randint(550,1000)
	return e
def calculateD(e, p, q):
	pq = (p-1)*(q-1)
	return p6.modularInverse(e, pq)
	
def generateKeys():
	p = randomPQ()
	q = randomPQ()
	e = randomE(p, q)
	d = calculateD(e, p, q)
	n = p * q
	return e, d, n

e, d, n = generateKeys()	
print 'Public key (e = ' + str(e) + ', n = ' + str(n) + ')'
print 'Private key (d = ' + str(d) + ', n = ' + str(n) + ')'
