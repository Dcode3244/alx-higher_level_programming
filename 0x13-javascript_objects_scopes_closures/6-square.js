#!/usr/bin/node

const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
