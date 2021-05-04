#!/usr/bin/node

const request = require('request');
request(process.argv[2], (err, data) => {
  if (err) {
    console.error('error:', err);
    return;
  }
  console.log(`code: ${data.statusCode}`);
});
