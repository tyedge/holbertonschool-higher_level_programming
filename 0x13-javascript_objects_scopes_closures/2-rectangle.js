#!/usr/bin/node

class Rectangle {
  constructor (wdth, hght) {
    if (wdth > 0 && hght > 0) {
      this.width = wdth;
      this.height = hght;
    }
  }
}
module.exports = Rectangle;
