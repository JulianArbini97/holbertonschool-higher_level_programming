#!/usr/bin/node
const arg = process.argv;
let i;

if (isNaN(arg[2]) === true) {
  console.log('Missing size');
} else {
  for (i = 0; i < arg[2]; i++) {
    console.log('X'.repeat(arg[2]));
  }
}
