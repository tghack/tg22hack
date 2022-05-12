#!/bin/bash

if [ "$#" != 1 ]; then
	echo "usage: $0 [infile]"
	exit
fi

pwd="$(zbarimg -q "$1" | cut -d: -f2 | base64 -d | cut -d' ' -f2)"
steghide extract -p "$pwd" -sf "$1" -xf outFlag.txt &> /dev/null
cat outFlag.txt
rm outFlag.txt
