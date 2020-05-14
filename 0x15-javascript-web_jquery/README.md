# 0x15. Javascript - Web JQuery [![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg?style=flat-square)](https://github.com/standard/semistandard)


In this chapter we learn about how to use an manipulate elements using Javascript and JQuery.


## General

+ How to select HTML elements in Javascript
+ How to select HTML elements with jQuery
+ What are differences between `ID`, `class` and `tag name` selectors
+ How to modify an HTML element style
+ How to get and update an HTML element content
+ How to modify the DOM
+ How to make a `GET` request with jQuery Ajax
+ How to make a `POST` request with jQuery Ajax
+ How to listen/bind to DOM events
+ How to listen/bind to user events


## Requirements

+ Allowed editors: `vi, vim, emacs`
+ All your files will be interpreted on Chrome (version 57.0)
+ All your files should end with a new line
+ Your code should be semistandard compliant with the flag --global `$: semistandard *.js --global $`
+ You must use `jQuery` version 3.x
+ You are not allowed to use `var`
+ HTML should not reload for each action: DOM manipulation, update values, `fetch data`


## More Info

### Import jQuery
```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```


## Tasks


### [0. No jQuery](0-script.js)
Script that updates the text color of the HTML tag `HEADER` to red `(#FF0000)`.


### [1. With jQuery](1-script.js)
Script that updates the text color of the HTML tag `HEADER` to red `(#FF0000)`, You cant use `document.querySelector` to select the HTML tag, You must use the `jQuery API`.


### [2. Click and turn red](2-script.js)
Script that updates the text color of the HTML tag `HEADER` to red `(#FF0000)` when the user clicks on the tag `DIV#red_header`.


### [3. Add `.red` class](3-script.js)
Script that updates the text color of the HTML tag `HEADER` to red `(#FF0000)` when the user clicks on the tag `DIV#red_header`. You must use the jQuery API.


### [4. Toggle classes](4-script.js)
Script that toggles the class of the HTML tag `HEADER` to red `(#FF0000)` when the user clicks on the tag `DIV#toggle_header`.


### [5. List of elements](5-script.js)
Script that adds a LI element to a list when the user clicks on the tag `DIV#add_item`.


### [6. Change the text](6-script.js)
Script that updates the text of the HTML tag `HEADER` to `New Header!!!` when the user clicks on `DIV#update_header`.


### [7. Star wars character](7-script.js)
Script that fetches and replaces the `name` of this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`.


### [8. Star Wars movies](8-script.js)
Script that fetches and lists all movies title by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`.


### [9. Say Hello!](9-script.js)
Script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of `hello` from that fetch in the HTMLs `tag DIV#hello`.


## Author
**_Jackson Moreno_**
