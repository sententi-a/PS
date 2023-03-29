// 스택 수열 https://www.acmicpc.net/problem/1874
// 스택을 사용해서 수열 nums를 만들 수 있냐!
// 스택에 push하는 순서는 반드시 오름차순!

const path =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/1874.txt`;
const fs = require("fs");
const input = fs.readFileSync(path).toString().trim().split("\n");

const count = parseInt(input[0]);
const nums = input.slice(1).map((elem) => parseInt(elem));
const stack = [];
const answers = [];

let lastPopped = 0;

for (let i = 0; i < count; i++) {
  let curr = nums[i];
  // 현재 보고 있는 원소가 마지막에 pop한 요소보다 크거나 같을 때
  if (curr >= lastPopped) {
    for (let j = lastPopped + 1; j < curr + 1; j++) {
      stack.push(j);
      answers.push("+");
    }

    if (curr === stack.pop()) {
      answers.push("-");
      lastPopped = curr; // 사실상 lastPushed와 같음
    } else {
      console.log("NO");
      return;
    }
  }
  //
  else {
    if (curr === stack.pop()) {
      answers.push("-");
      //   lastPopped = curr;
    } else {
      console.log("NO");
      return;
    }
  }
}

console.log(answers.join("\n"));
