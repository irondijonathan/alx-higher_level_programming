#!/usr/bin/node

let second;
let first;

if (process.argv.length < 4) {
  second = 0;
} else {
  second = parseInt(process.argv[2]);
  first = parseInt(process.argv[3]);
  if (first < second) {
    const tmp = first;
    first = second;
    second = tmp;
  }
}
for (let i = 4; i < process.argv.length; i++) {
  const curr = parseInt(process.argv[i]);
  if (curr > first) {
    second = first;
    first = curr;
  } else if (curr > second && curr < first) {
    second = curr;
  }
}
console.log(second);
