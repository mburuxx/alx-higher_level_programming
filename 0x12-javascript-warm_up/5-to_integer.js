#!/usr/bin/node

const args = parseInt(process.argv[2]);

if (Number.isInteger(args)) {
  console.log('My number: ' + args);
} else {
  console.log('Not a number');
}
