# 0x14. Javascript - Web scraping
[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg?style=flat-square)](https://github.com/standard/semistandard)


Web scraping is a technique used for retrieving data from websites. You fetch the pages contents, and then extract the data you need from the page for processing, saving it, or simply displaying it on your app. It comes in handy when the app/website you are trying to scrape does not expose any external API for public consumption. It is worth noting that some sites do not allow scraping, so be aware of that before you attempt it.

## General


+ How to manipulate `JSON` data
+ How to use `request` and `fetch API`
+ How to read and write a file using `fs` module


## Requirements


+ Allowed editors: `vi, vim, emacs`
+ All your files will be interpreted on `Ubuntu 14.04 LTS` using node (version 10.14.x)
+ All your files should end with a new line
+ The first line of all your files should be exactly `#!/usr/bin/node`
+ Your code should be `semistandard` compliant.
+ All your files must be executable
+ The length of your files will be tested using `wc`
+ You are not allowed to use `var`


### Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

```
$ sudo npm install semistandard --global
```

### Install `request` module and use it

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks


### [0. Readme](0-readme.js)
Script that reads and prints the content of a file.


### [1. Write me](1-writeme.js)
Script that writes a string to a file.


### [2. Status code](2-statuscode.js)
Script that display the status code of a GET request.


### [3. Star wars movie title](3-starwars_title.js)
Script that prints the title of a Star Wars movie where the episode number matches a given integer.


### [4. Star wars Wedge Antilles](4-starwars_count.js)
Script that prints the number of movies where the character Wedge Antilles is present.


### [5. Loripsum](5-request_store.js)
Script that gets the contents of a webpage and stores it in a file.


### [6. How many completed?](6-completed_tasks.js)
Script that computes the number of tasks completed by user id.


## Author
**_Jackson Moreno_**
