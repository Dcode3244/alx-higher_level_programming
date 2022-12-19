#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  let args = process.argv.map(Number);
  args = args.slice(2);
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
