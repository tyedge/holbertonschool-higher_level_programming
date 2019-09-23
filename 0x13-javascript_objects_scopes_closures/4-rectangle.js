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

  rotate () {
    const myVar = this.width;
    this.width = this.height;
    this.height = myVar;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
