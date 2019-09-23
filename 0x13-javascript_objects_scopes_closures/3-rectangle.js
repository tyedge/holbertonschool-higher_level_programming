#!/usr/bin/node

class Rectangle {
  constructor (wdth, hght) {
    if (wdth > 0 && hght > 0) {
      this.width = wdth;
      this.height = hght;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
