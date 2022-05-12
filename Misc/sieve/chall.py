#!/bin/python3
from random import randint

flag = "TG22{E7_G4n5k3_L4ng7_Og_V4n5k311g_F14gg_:)}".upper()

outp = ""
i = 0
while i < len(flag):
	for _ in range(randint(1, 100)):
		outp += chr(randint(97, 97+25))
	outp += flag[i]
	i += 1

print(outp)
