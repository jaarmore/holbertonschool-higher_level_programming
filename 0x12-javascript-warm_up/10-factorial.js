#!/usr/bin/node
function factorial (myValue) {
  if (isNaN(myValue) || parseInt(myValue) === 0) {
    return 1;
  }
  return parseInt(myValue) * factorial(parseInt(myValue) - 1);
}
const args = process.argv;
console.log(factorial(args[2]));
