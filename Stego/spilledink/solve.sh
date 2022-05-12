#!/bin/bash

if [ "$#" != 1 ]; then
	echo "usage: $0 file"
	exit
fi

convert "$1" -fuzz 0% -opaque "#FEFEFE" -fill "#000000" exported-tmp-file.png
convert -swirl -90 exported-tmp-file.png outfile-tmp-file.png
zbarimg -q outfile-tmp-file.png | cut -d: -f2 | base64 -d

rm exported-tmp-file.png
rm outfile-tmp-file.png
