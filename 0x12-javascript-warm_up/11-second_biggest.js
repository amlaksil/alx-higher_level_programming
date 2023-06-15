#!/usr/bin/node

const len = process.argv.length;
if (len === 2 || len === 3) console.log(0);
else {
  const list = process.argv.slice(); /* or use [ ...process.argv] to copy an array */
  for (let i = 0; i < 2; i++) {
    for (let j = 2; j < len - i; j++) {
      if (parseInt(list[j]) > parseInt(list[j + 1])) {
        const tmp = list[j + 1];
        list[j + 1] = list[j];
        list[j] = tmp;
      }
    }
  }
  console.log(list[len - 2]);
}
