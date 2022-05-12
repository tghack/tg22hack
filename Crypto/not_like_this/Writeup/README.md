> Author: Solli#0387

## PatchNotes

## Chall
### Description

    Another attempt at making a simple encryption scheme,

    I think it would have been good around 27 BC


### Solution

The challenge performs a ceasar cipher on hex values. 

To solve this one can do the following:

1. Find the difference from the `known` values in the flag which is `TG22{}`
2. Once the difference is found a decrypter can be written, or the encryptor itself can be used to decrypt with the correct difference. 


Correct value offset was 999, but there are lower values which also will work due to hex only having 256 values.  


Flag: `TG22{just_a_little_rot13_in_hex}`
