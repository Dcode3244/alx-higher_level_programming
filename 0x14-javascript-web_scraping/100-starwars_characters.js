#!/usr/bin/node

const request = require('request');

const requestCallback = (err, response, body) => {
  if (err) { console.error(err); }

  const films = JSON.parse(body);

  films.characters.map((character) => (
    request(character, function (e, r, b) {
      if (e) { return console.error(e); }
      console.log(JSON.parse(b).name);
    })
  ));
};

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, requestCallback);
