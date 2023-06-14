#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) this.print();
    else {
      for (let i = 0; i < this.size; i++) {
        let s = '';
        for (let j = 0; j < this.size; j++) {
          s += 'C';
        }
        console.log(s);
      }
    }
  }
}
module.exports = Square;
