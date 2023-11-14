#!/usr/bin/node

// This Defines a Rectangle class with width and height attributes.

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
