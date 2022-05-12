# Assev blog

Inneholder 2 flag (options er broken atm...), hovedoppgaven er Bruteforce m/ robots som secret

## Bruteforce
### Oppgave
Bryt deg inn på bloggen til Assev! `url`

### Løsning
Blog siden inneholder all informasjon som trengs for å løse oppgaven. "Skrevet av" hinter til at brukernavnet er `assev`.
Passordet finner de ved å lage egen dictionary, dekryptere Caesar cipheren, og bruke det nevnte hashcat regelsettet for å utvide dictionary. Intended solution er derfor at de scraper bloggen og gjør en online bruteforce med typ Hydra/Python script.

`FLAG: RIP_DAT234{STRONG_PASSWORDS_BE_STRONG!}`

## Robots
### Oppgave
Det er et hemmelig flag på blogsiden, kan du finne det?

### Løsning
Går enn til /robots.txt så er første hintet at den returnerer HTML og ikke plaintext. Det skjuler seg nemling noe i HTML comments! Det random genereres `<!-- n c -->` der `n` er posisjon i stringen, og `c` er character. Bare loope nok ganger så får enn satt sammen flagget.

`FLAG: RIP_DAT234{HELLO_TO_ALL_THE_ROBOTS_IN_DA_HOUSE!}`


