#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    let cont = 0;
    for (cont = 0; cont < this.height; cont++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
