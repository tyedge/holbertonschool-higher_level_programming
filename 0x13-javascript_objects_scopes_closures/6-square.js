#!/usr/bin/node

class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let a = 0; a < this.width; a++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
