// 분해합 https://www.acmicpc.net/problem/2231

const path = process.platform === "linux" ? "/dev/stdin" : "Baekjoon/2231.txt";
const fs = require("fs");
// const input = parseInt(fs.readFileSync(path).toString().trim());
const input = fs.readFileSync(path).toString().trim();
const target = parseInt(input);
const digit = input.length; //자리수
let answer = 0;

function getDigitSum(n) {
  let result = n;
  let tempNum = n;

  while (tempNum > 0) {
    result += tempNum % 10;
    tempNum = Math.floor(tempNum / 10);
  }
  //   console.log(n, result);
  return result;
}
// for (let i = target - 9 * digit; i < target; i++) {
for (let i = target - 9 * digit; i <= target; i++) {
  if (getDigitSum(i) === target) {
    answer = i;
    break;
  }
}

console.log(answer);
