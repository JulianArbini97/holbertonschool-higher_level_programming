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

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
