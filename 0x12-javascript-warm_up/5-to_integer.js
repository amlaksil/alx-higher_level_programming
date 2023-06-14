#!/usr/bin/node

if (process.argv[2] === undefined && process.argv[3] === undefined) {
  console.log('Not a number');
} else if (isNaN(process.argv[2]) === true) console.log('Not a number');
else console.log(`My number: ${process.argv[2]}`);
