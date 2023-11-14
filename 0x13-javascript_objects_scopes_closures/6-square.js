#!/usr/bin/node

const SquareOld = require('./5-square');

module.exports = class Square extends SquareOld {
  charPrint (c) {
    super.print(c);
  }
};
