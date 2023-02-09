#!/usr/bin/node

const request = require('request');

const reducer = (count, result) => (
  result.characters.find((char) => char.endsWith('/18/')) ? ++count : count
);

const requestCallback = (err, response, body) => {
  if (err) { console.error(err); }

  const results = JSON.parse(body).results;
  console.log(results.reduce(reducer, 0));
};

request(process.argv[2], requestCallback);
