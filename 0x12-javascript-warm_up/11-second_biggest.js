#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const args = [];
  for (let i = 2; i < process.argv.length; i++) {
    args.push(Number(process.argv[i]));
  }
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
