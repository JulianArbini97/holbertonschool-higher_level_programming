#!/usr/bin/node
const arg = process.argv;

if (isNaN(arg[2]) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg[2]);
}
