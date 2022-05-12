import requests
from time import sleep
import re
flag = ['?' for _ in range(50)]
regex = re.compile(r"<!-- (?P<pos>\d+)\s(?P<ch>.)\s-->")

for i in range(500):
    resp = requests.get('http://localhost:5000/robots.txt')
    if resp.status_code != 200:
        continue
    cap = regex.search(resp.text)
    flag[int(cap['pos'])] = cap['ch']
    print(f"\r{''.join(flag)}", end='')
    sleep(0.1)
