#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  const myVar = parseInt(args[2]);
  if (myVar > 0) {
    for (let i = 0; i < myVar; i++) {
      console.log('C is fun');
    }
  }
}
