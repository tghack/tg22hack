#!/usr/bin/env python

from random import randint

flg = "84 71 50 50 123 104 117 114 114 52 95 100 117 95 104 106 52 108 112 95 107 118 52 107 107 95 107 118 52 107 107 95 229 95 107 48 109 109 51 95 104 106 51 109 125"

RAND_SOFTWARE = ["firefox", "notepad", "edge", "explorer", "msfvenom", "powershell", "cmd", "winGet"]
DOMAINS = ["youtube.com", "gathering.org", "duckduckgo.com", "google.com", "tghack.no", "github.com", "twitter.com/tghack_ctf",]

def DUCKS(prog, streng):
	return f"""
GUI r
DELAY 50
STRING {prog}.exe
ENTER
DELAY 100
STRING https://{streng}/
"""

def FLG_DUCK(dly, strr):
	return f"""
DELAY {dly}
STRING {strr}
ENTER
"""

for k in reversed(flg.split(' ')):
	decoy  = int(k) + randint(10,120)
	print (FLG_DUCK(decoy, k))