#!/usr/bin/node

let x = process.argv[2];
if (process.argv[2] === undefined) console.log('Missing number of occurrences');
if (x > 0) {
  while (x >= 1) {
    console.log('C is fun');
    x--;
  }
}
