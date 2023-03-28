// 그룹 단어 체커 https://www.acmicpc.net/problem/1316
// 단어에 존재하는 모든 문자에 대해, 각 문자가 연속해서 나타나는 경우 카운트

const path =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/1316.txt`;
const fs = require("fs");
const input = fs.readFileSync(path).toString().trim().split("\n");

const num = parseInt(input[0]);
const words = input.slice(1);
let answer = 0;

for (let i = 0; i < num; i++) {
  const word = words[i].split("");
  const dict = {};
  let flag = true;

  while (word.length) {
    let char = word.pop();
    if (!dict[char]) {
      dict[char] = 1;
      while (word.length && word[word.length - 1] === char) {
        word.pop();
      }
    } else {
      flag = false;
      break;
    }
  }

  if (flag) answer += 1;
}

console.log(answer);
