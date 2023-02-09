#!/usr/bin/node

const request = require('request');

const callback = (err, response, body) => {
  if (err) {
    return console.error(err);
  }
  console.log(JSON.parse(body).title);
};

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, callback);
