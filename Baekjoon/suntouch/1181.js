// 단어 정렬 https://www.acmicpc.net/problem/1181

const path =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/1181.txt`;

const fs = require("fs");
let input = fs.readFileSync(path).toString().trim().split("\n");

n = parseInt(input[0]);

input = [...new Set(input.slice(1))];
// console.log(input);

input.sort().sort((a, b) => a.length - b.length);
// console.log("no" > "im");
input.forEach((elem) => console.log(elem));
