// 크로아티아 알파벳 https://www.acmicpc.net/problem/2941

// 목록에 있는 알파벳은 접미사가 = / - / j

const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "Baekjoon/2941.txt";
const input = fs.readFileSync(path).toString().trim();

const stack = input.split(""); // string to array
// console.log(stack);

let answer = 0;

while (stack.length) {
  //   console.log(stack);
  let char = stack.pop();
  let top = stack.length - 1;
  answer += 1;
  //   console.log(stack);

  if (char === "-") {
    stack.pop();
  } else if (char === "j") {
    if (stack.length && (stack[top] === "l" || stack[top] === "n")) {
      stack.pop();
    }
  } else if (char === "=") {
    if (stack.length && (stack[top] === "c" || stack[top] === "s")) {
      stack.pop();
    } else if (stack.length && stack[top] === "z") {
      stack.pop();
      top = stack.length - 1;
      if (stack.length && stack[top] === "d") {
        stack.pop();
      }
    }
  }

  //   console.log(answer);
}

console.log(answer);
