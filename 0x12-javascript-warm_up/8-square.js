#!/usr/bin/node

if (!Number(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = Number(process.argv[2]); i > 0; i--) {
    let width = '';
    for (let i = Number(process.argv[2]); i > 0; i--) {
      width += 'X';
    }
    console.log(width);
  }
}
