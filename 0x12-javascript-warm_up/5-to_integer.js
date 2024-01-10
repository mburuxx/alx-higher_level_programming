#!/usr/bin/node
console.log(isNaN(parseInt(process.argv[2])) ? 'Not a number' : 'My number: ' + parseInt(process.argv[2]));

/*
* const num = Math.floor(Number(process.argv[2]));
* console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
*/
