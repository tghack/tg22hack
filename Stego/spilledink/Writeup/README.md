# nonhosted-template
> Author: nonhosted-template

## PatchNotes

## Chall
### Description


### Solution

Opened image in photopea (web photoshop copycat)
Selected the Color replacement tool under the brush category
Size: 1000, Blend-mode: Luminosity, Mode: Background, Tolerance: 0
Hint for this is that you can see the white parts of the image are both #ffffff and #fefefe. But stegsolve doesn't catch this.

Then recolor everything, the qr code will emerge.
Then afterwards hit ctrl+a, then ctrl+i to invert the color in the selection
Then I re-colored the ink, black. Because the black outline around the white spots could confuse the QR code regeneration.
Then export the image

Or use convert

`$ convert inked-document.png -fuzz 0% -opaque "#FEFEFE" -fill "#000000" exported.png`

Next we can see that the image is swirled. Use ImageMagick's convert to swirl it back.
Looks like about 90 deg because of the square in the middle sitting correctly

`$ convert -swirl -90 exported.png outfile.png`

Then since qr codes are regenerative we can try to read it with zbarimg.

`$ zbarimg -q outfile.png`

And it's readable

base64 decode the text and you have the flag.

`$ zbarimg -q outfile.png | cut -d":" -f2 | base64 -d`
