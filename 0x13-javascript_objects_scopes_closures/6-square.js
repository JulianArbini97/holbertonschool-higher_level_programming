#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let cont = 0;
    for (cont = 0; cont < this.height; cont++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tempw = this.width;
    const temph = this.height;
    this.width = temph;
    this.height = tempw;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    let i = 0;
    if (c == null) {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
