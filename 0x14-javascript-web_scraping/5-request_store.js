#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const requestCallback = (err, response, body) => {
  if (err) { console.error(err); }

  fs.writeFile(process.argv[3], body, function (err) {
    if (err) { console.error(err); }
  });
};

request(process.argv[2], requestCallback);
