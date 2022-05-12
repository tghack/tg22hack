> Author: Solli#0387

## Chall
### Description

    Ceasar proivded me with a message before the competition began.

    Can you help me read the contents?


### Solution

The file attached is a file where each byte is increased by a value of 13. This rotates to 0 if it overflows `ff` in hex. 
So in short it is a png. file which has been performed rot13 with hex on.

The filename is also a hint to what the file will result in:

`synt.cat` + rot13 = `flag.png`
