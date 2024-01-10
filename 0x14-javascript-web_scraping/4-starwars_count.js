#!/usr/bin/node

const request = require('request');
let count = 0;

request.get(process.argv[2], (_err, response, body) => {
  if (_err) {
    console.log(_err);
  } else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.search(/18/g) !== -1) {
          count = count + 1;
        }
      }
    }
  }
  console.log(count);
});
