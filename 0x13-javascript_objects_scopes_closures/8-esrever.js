#!/usr/bin/node

exports.esrever = function (list) {
  const myArray = [];
  for (let i = 0; i < list.length; i++) {
    myArray.unshift(list[i]);
  }
  return myArray;
};
