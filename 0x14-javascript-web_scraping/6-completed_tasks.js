#!/usr/bin/node

const request = require('request');

const requestCallback = (err, response, body) => {
  if (err) { console.error(err); }

  const todos = JSON.parse(body);
  const comp = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (!comp[todo.userId]) { comp[todo.userId] = 0; }
      comp[todo.userId]++;
    }
  }

  console.log(comp);
};

request(process.argv[2], requestCallback);
