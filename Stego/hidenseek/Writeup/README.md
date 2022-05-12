# nonhosted-template
> Author: nonhosted-template

## PatchNotes

## Chall
### Description


### Solution

zbarimg -q hidenseek.jpg | cut -d: -f2 | base64 -d
steghide extract -p somethingHidden -sf hidenseek.jpg

har laget scripts nå
