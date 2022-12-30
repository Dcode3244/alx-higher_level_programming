#!/usr/bin/node

const dict = require('./101-data').dict;

const ids = [...new Set(Object.values(dict))];
const newD = {};
for (const id of ids) {
  newD[id] = [];
}

for (const key in dict) {
  newD[dict[key]].push(key);
}
console.log(newD);
