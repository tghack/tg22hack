from secret import *

enc = [0] * len(flag)
for i in range(len(flag)):
    enc[-(i+1)] = (ord(flag[i]))

cne2 = []
for e in range (0,len(enc),2):
    cne2.append(enc[e]+secret_number_1)

for e in range (1,len(enc),2):
    cne2.append(enc[e]-secret_number_2)

for r in cne2:
    print(hex(r))
