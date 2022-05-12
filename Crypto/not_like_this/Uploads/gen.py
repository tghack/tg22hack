from secret import *

rotated_hex = []
for i in range(256):
    rotated_hex.append(('{:02X}'.format(i)))

enc = []
for i in flag:
    enc.append((ord(i)))

cne = enc[::-1]
encrypted_flag = []
for a in cne:
    int_val = a
    formatted_val = (('{:02X}'.format(int_val)))
    test = (rotated_hex[(rotated_hex.index(formatted_val) + secret_number) % 256])
    encrypted_flag.append(test)

for r in encrypted_flag:
    print(hex(int(r,16)))