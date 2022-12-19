#!/usr/bin/node

if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let i = Number(process.argv[2]); i > 0; i--) {
    console.log('C is fun');
  }
}
