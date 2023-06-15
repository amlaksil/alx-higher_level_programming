#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) === true) return (1);
  if (+num === 0) return (1);
  const fact = (+num * factorial(+num - 1));
  return (fact);
}
const num = process.argv[2];
const result = factorial(num);
console.log(result);
