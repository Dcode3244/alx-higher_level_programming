#!/usr/bin/node

const request = require('request');
let count = 0;

const callback = (err, response, body) => {
  if (err) { return console.error(err); }
  const results = JSON.parse(body).results;
  for (const result of results) {
    for (const character of result.characters) {
      if (character.includes('/people/18/')) {
        count++;
      }
    }
  }
  console.log(count);
};

request(process.argv[2], callback);
