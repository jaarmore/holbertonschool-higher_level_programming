#!/usr/bin/node
/*
 * Script that reads and prints the content of a file.
 */
const args = process.argv;
const fs = require('fs');

fs.readFile(args[2], 'utf-8', function (error, data) {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
