// 한수 https://www.acmicpc.net/problem/1065

const path =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/1065.txt`;

const fs = require("fs");
let input = fs.readFileSync(path).toString().trim();
const digit = input.length;
input = parseInt(input);
let answer = 0;

// 일단 한 자리수, 두 자리수까지는 모두 한수
// n은 최대 세 자리수 (사실상 1000까지이지만 1000은 한수가 아니므로 무시)
function isHansu(n) {
  let nums = n.toString().split("");
  let difference = nums[1] - nums[0];
  for (let i = 2; i < nums.length; i++) {
    if (nums[i] - nums[i - 1] !== difference) {
      return false;
    }
  }
  return true;
}

if (digit <= 2) {
  answer = input;
}

// 100 ~ 1000
else {
  answer = 99;
  for (let i = 100; i <= input; i++) {
    if (isHansu(i)) {
      answer += 1;
    }
  }
}

console.log(answer);
