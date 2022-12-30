#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map((num, idx) => num * idx);
console.log(list);
console.log(newList);
