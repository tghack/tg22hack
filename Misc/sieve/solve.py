#!/bin/python3


with open(input("Filename? "), "r") as f:
	inp = f.read()

out = ""
for letter in inp:
	if not letter.islower():
		out += letter

print(out)
