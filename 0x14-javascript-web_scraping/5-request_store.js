#!/usr/bin/node

const request = require('request');
const fs = require('fs');
let data;

request.get(process.argv[2], (_err, response, body) => {
  if (_err) {
    console.log(_err);
  } else {
    data = body;
    fs.writeFile(process.argv[3], data, { encoding: 'utf8' }, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
