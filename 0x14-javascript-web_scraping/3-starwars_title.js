#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (_err, response, body) => {
  if (_err) {
    console.log(_err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
