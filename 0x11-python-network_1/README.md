# 0x11. Python - Network #1


## General

+ How to fetch internet resources with the Python package `urllib`
+ How to decode `urllib` body response
+ How to use the Python package `requests` #requestsiswaysimplerthanurllib
+ How to make HTTP `GET` request
+ How to make HTTP `POST`/`PUT`/etc. request
+ How to fetch JSON resources
+ How to manipulate data from an external service


## Requirements

+ Allowed editors: `vi, vim, emacs`
+ All your files will be interpreted/compiled on `Ubuntu 14.04 LTS` using `python3 (version 3.4.3)`
+ All your files should end with a new line
+ The first line of all your files should be exactly `#!/usr/bin/python3`
+ Your code should use the `PEP 8` style (version 1.7.*)
+ All your files must be executable
+ The length of your files will be tested using `wc`


## Tasks


### [0. What's my status? #0](0-hbtn_status.py)
Python script that fetches `https://intranet.hbtn.io/status`


### [1. Response header value #0](1-hbtn_header.py)
Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.


### [2. POST an email #0](2-post_email.py)
Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter.


### [3. Error code #0](3-error_code.py)
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).


### [4. What's my status? #1](4-hbtn_status.py)
Python script that fetches `https://intranet.hbtn.io/status`.


### [5. Response header value #1](5-hbtn_header.py)
Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header.


### [6. POST an email #1](6-post_email.py)
Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter.


### [7. Error code #1](7-error_code.py)
Python script that takes in a URL, sends a request to the URL and displays the body of the response.


### [8. Search API](8-json_api.py)
Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.


### [9. My Github!](10-my_github.py)
Python script that takes your Github credentials (username and password) and uses the `Github API` to display your id.


## AUTHOR
**_Jackson Moreno_**
