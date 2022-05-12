> Author: Solli#0387

## Chall
### Description

This should be convoluted enough so that you cant decode the message, right?

### Solution

To solve this one has to be aware of that one has a few `known` values from the start, even though none are provided. 

1. The flag format is known `TG22{}`
2. The length of the flag is known

Due to these two knowns one can place the values of `TG22{}` in the correct location in the encoded text, and using that one can find both the unknown values by checking the offset of the ascii values of the known values and the encoded values.

In the code the following happens:

1. The flag is first read and stored in an array in a reverse order. 
2. The reversed flag values of index 0,2,4 ... and so on is added to a new list, with a secret value added to the ascii value.
3. The reversed flag values of index 1,3,5 ... and so on is added to a new list, with a secret value substracted from the ascii value.

By using these steps one can know some locations of the original flag, and by that know the new values.

In the original flag `}` is tha last value, and will be places at the start when reversed. This value will then be at index 0 of the new array which is used in the next step. 

The value of `}` is 125, but we see that in the output the first value is 0x83 == 131. This is due to the secret value which is added to this letter. We now know that `secret_number_1` == 6.

Since the flag is reversed, and we have all the odd numbers of the index at the end, we can know that the last letter in the output should represent the `T` in the original flag. The value of `T` is 84, and the last value in the output is 76. From this we know that `secret_number_2` == 8.

Using these together with the pattern which the values is scrambled in we can reconscrut the flag and get the flag.

Flag: `TG22{well_well_that_wasnt_to_hard}`
