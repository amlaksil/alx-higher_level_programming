#!/usr/bin/node
const SquareF = require('./5-square');

class Square extends SquareF {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
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
