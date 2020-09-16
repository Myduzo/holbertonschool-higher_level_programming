#!/usr/bin/node
const num = Number(process.argv[2]);

if (isNaN(num) || num === 1) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  const max = list.sort((a, b) => b - a)[1];
  console.log(max);
}
