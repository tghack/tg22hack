> Author: Solli#0387

## Chall
### Description
    Here at TG we have created a homepage for our own label makers.

    Could you check it for vulnerabilities before it goes into production?

    **Flag at /flag**

    Link: labelfabricinc.chall.tghack.no


### Solution


Notice that when going to the page your URL will have changed to something containing: `?page=`.


This looks like a direct LFI vulnerablity which can be exploited by referencing the file one would like to view.


Flag would be at: `http://labelfabricinc.chall.tghack.no/?page=/flag`


Flag: `TG22{get_me_that_file!}`
