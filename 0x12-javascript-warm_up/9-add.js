#!/usr/bin/node

let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);

function add(a, b) {
  return a + b;
}

if (Number.isInteger(a) && Number.isInteger(b)) {
  console.log(add(a, b));
} else {
  console.log('NaN');
}
