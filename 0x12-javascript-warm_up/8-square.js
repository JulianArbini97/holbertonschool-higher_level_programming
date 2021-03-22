#!/usr/bin/node
const arg = process.argv;
let i;

if (isNaN(arg[2])) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < arg[2]; i++) {
    console.log('X'.repeat(arg[2]));
  }
}
