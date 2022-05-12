
rotated_hex = []

for i in range(256):
    rotated_hex.append(('{:02X}'.format(i)))

with open('flag.png','rb') as file:
    hex_list = file.read()

out_hex = ['{:02X}'.format(b) for b in hex_list]

byte_str = b''
for a in out_hex:
    int_val = (int(a,16))
    formatted_val = (('{:02X}'.format(int_val)))
    rotated_val = (rotated_hex[(rotated_hex.index(formatted_val) + 13) % 256])
    byte_str += bytes.fromhex(rotated_val)

with open("synt.cat", "wb") as binary_file:
    binary_file.write(byte_str)