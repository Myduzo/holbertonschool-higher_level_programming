#!/usr/bin/node
const num = process.argv.slice(2);

if (num <= 3) {
  console.log('0');
} else {
  const list = process.argv.slice(2);
  const max = list.sort((a, b) => b - a)[1];
  console.log(max);
}
