#!/usr/bin/node
/*
 * script that updates the text color of the HTML tag HEADER to red (#FF0000)
 * You must use document.querySelector to select the HTML tag
 * Note: Your script must be imported from the HEAD tag, not at the end of the HTML.
 */
document.addEventListener('DOMContentLoaded', function () {
  const elem = document.querySelector('header');
  elem.style.color = '#FF0000';
});
