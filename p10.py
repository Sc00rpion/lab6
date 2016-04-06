#!/usr/bin/python

import sys
import string
import random

from Crypto.PublicKey import RSA

# Tworzenie kluczy RSA
rsa_keys = RSA.generate(1024)

# Wydzielenie klucza publicznego
pub_key = rsa_keys.publickey()
text = open(sys.argv[1]).read()
print text
# Zaszyfrowanie przy pomocy klucza publicznego
encrypted = pub_key.encrypt(text, "some randomness") 
print encrypted
# Odszyfrowanie kluczem prywatnym
print rsa_keys.decrypt(encrypted)
print 'Public key: (n: ' + str(rsa_keys.key.n) + ', e: ' + str(rsa_keys.key.e) + ')'
print 'Private key: (n: ' + str(rsa_keys.key.n) + ', d: ' + str(rsa_keys.key.d) + ')'

