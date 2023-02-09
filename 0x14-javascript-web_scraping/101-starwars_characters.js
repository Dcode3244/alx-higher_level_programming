#!/usr/bin/node

const request = require('request');

const requestCharacter = (characters, idx) => {
  request(characters[idx], function (e, r, b) {
    if (e) { return console.error(e); }
    console.log(JSON.parse(b).name);
    if (idx < characters.length - 1) {
      return requestCharacter(characters, ++idx);
    }
  });
};

const requestCallback = (err, response, body) => {
  if (err) { console.error(err); }

  const films = JSON.parse(body);

  requestCharacter(films.characters, 0);
};

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, requestCallback);
