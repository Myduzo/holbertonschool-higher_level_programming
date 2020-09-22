#!/usr/bin/node
const request = require('request');
const todos = process.argv[2];

request.get(todos, (err, res, body) => {
  const data = JSON.parse(body);
  if (err) {
    console.error(err);
  }
  const list = {};
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed) {
      if (!(data[i].userId in list)) {
        list[data[i].userId] = 0;
      }
      list[data[i].userId] += 1;
    }
  }
  console.log(list);
});
