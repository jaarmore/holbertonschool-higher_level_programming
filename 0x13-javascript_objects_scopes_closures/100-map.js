#!/usr/bin/node

const list = require('./100-data').list;
const myList = list.map((num, index) => num * index);

console.log(list);
console.log(myList);
