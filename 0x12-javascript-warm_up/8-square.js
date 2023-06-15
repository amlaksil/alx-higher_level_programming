#!/usr/bin/node

if (process.argv[2] === undefined || (isNaN(process.argv[2]) === true)) {
  console.log('Missing size');
} else {
  const size = process.argv[2];
  for (let i = 0; i < size; i++) {
    let c = '';
    for (let j = 0; j < size; j++) c += 'X';
    console.log(c);
  }
}
