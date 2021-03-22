#!/usr/bin/node
const arg = process.argv;
let i;

if (isNaN(arg[2]) === true) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < arg[2]; i++) {
    console.log('C is fun');
  }
}
