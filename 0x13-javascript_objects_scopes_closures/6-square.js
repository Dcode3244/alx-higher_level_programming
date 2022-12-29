#!/usr/bin/node

const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (c) {
    const ch = c ? 'C' : 'X';
    for (let i = 0; i < this.height; i++) {
      const rows = [];
      for (let j = 0; j < this.width; j++) {
        rows.push(ch);
      }
      console.log(rows.join(''));
    }
  }
};
