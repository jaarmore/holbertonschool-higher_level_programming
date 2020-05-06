#!/usr/bin/node
const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  const params = args.slice(2).map(Number);
  params.sort(function (a, b) { return a - b; });
  const second = params.length - 2;
  console.log(params[second]);
}
