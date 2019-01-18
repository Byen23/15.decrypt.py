# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17, 2019

File: decrypt.py
Decrypts an input string of lowercase letters and print
the result. THe other input is the distance value.
@author: Byen23
"""
# This will be my 14th program to be uploaded on Github.

code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in code:
	ordvalue = ord(ch)
	cipherValue = ordvalue - distance
	if cipherValue < ord('a'):
		cipherValue = ord('z') - \
		              (distance - (ord('a') - ordvalue - 1))
	plainText += chr(cipherValue)
print(plainText)

