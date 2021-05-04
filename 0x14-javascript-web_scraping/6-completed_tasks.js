#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, data, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const tasks = JSON.parse(body);
  const dicTasks = {};
  let cont = 0;
  const lenlist = tasks.length;
  for (cont = 0; cont < lenlist; cont++) {
    if (tasks[cont].completed) {
      if (!dicTasks[tasks[cont].userId]) {
        dicTasks[tasks[cont].userId] = 0;
      }
      dicTasks[tasks[cont].userId] += 1;
    }
  }
  console.log(dicTasks);
});
