#!/usr/bin/node

const fs = require('fs');

const callback = (err) => {
  if (err) {
    return console.error(err);
  }
};

fs.writeFile(process.argv[2], process.argv[3], callback);
