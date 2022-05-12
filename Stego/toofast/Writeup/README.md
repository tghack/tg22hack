# nonhosted-template
> Author: nonhosted-template

## PatchNotes

## Chall
### Description
En GIF fil hvor alle bokstavene vises alt for raskt til å leses vanlig.

### Solution
Kan bruke en nettside som denne
    https://ezgif.com/speed/ezgif-3-795f0dfd2f3c.gif
    Og bare gjøre farten til 1% av tiden den egt bruker.
    men vanskelig å telle antall '1'-ere.

Noe som denne siden
    https://onlinegiftools.com/change-gif-duration
    Viser faktisk details om hver frame, og bla. for '1' da viser den 50ms delay i forhold til vanlid 10. som viser det er 5*'1' i gifen

Beste solution er å extracte alle bildene i gifen tbh, så onlinetools for å se på duration
Løsninger som `convert flag.gif target.png` lager bare masse target-0..20.png bilder i dir, men tenker ikke på duplicates
Slow down metoden viser da at det er flere like, så det er ikke for vanskelig å få tak i hele flagget
