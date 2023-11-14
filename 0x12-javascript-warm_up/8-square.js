#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (size === undefined || isNaN(size)) {
  console.log('Missing size');
}
let line = '';
for (let i = 0; i < size; i++) {
  line += 'X';
}
for (let j = 0; j < size; j++) {
  console.log(line);
}
