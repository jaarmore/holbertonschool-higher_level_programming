#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;