#!/usr/bin/node

const request = require('request');
const data = {};

request.get(process.argv[2], (_err, response, body) => {
  if (_err) {
    console.log(_err);
  } else {
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed === true) {
        if (data[task.userId] === undefined) {
          data[task.userId] = 1;
        } else {
          data[task.userId]++;
        }
      }
    }
    console.log(data);
  }
});
