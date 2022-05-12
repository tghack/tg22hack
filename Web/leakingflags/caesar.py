from string import ascii_lowercase as al, ascii_uppercase as au
al = al + 'æøå'
au = au + 'ÆØÅ'
string = 'Denne teksten er kryptert med nøkkel 25, for ekstra vanskelighetsgrad så har vi også brukt æøå i tegnsettet! Hvis du klarer å lese dette er det veldig bra!'
def encrypt(s, k):
    e = ''
    for c in s:
        if c in al:
            e += al[(al.index(c)+k)%len(al)]
        elif c in au:
            e += au[(au.index(c)+k)%len(au)]
        else:
            e += c
    return e
print(encrypt(string, 25))





