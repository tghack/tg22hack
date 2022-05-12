> Author: Solli#0387

## Chall
### Description
    I have made an application to send some data, however I am still getting errors. 

    Can you fix it for me?

    Link: ``postoffice.chall.tghack.no``


### Solution

The request made by the browser is using the wrong header for the data type it is sending. 

Change the header to `Content-Type: application/json` and send some valid JSON and the flag will be provided.

This can be done by copying the request from the network tab in the browser.
1. Copy request as cURL
2. Change request Content-Type to `Content-Type: application/json`
3. Make request with cURL

Flag: `TG22{that_was_some_good_data}`

