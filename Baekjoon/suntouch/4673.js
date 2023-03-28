// 셀프 넘버 https://www.acmicpc.net/problem/4673
// 양의 정수 n에 대해 d(n) = n + n의 각 자리수들

// const path =
//   process.platform === "linux" ? "/dev/stdin" : `${__dirname}/4673.txt`;

// const fs = require("fs");
// const input = fs.readFileSync(path).toString().trim();

// 생성자가 없는 숫자를 셀프넘버...!
// 10000보다 작거나 같은 셀프넘버를 한 줄에 하나씩 출력하는 프로그램

const maxNum = 10000;
function getDigitSum(n) {
  let result = n;
  let temp = n;

  while (temp > 0) {
    result += temp % 10;
    temp = Math.floor(temp / 10);
  }

  return result;
}

function isSelfNumber(n) {
  const stringNum = n.toString();
  const digit = stringNum.length;

  for (let i = n - digit * 9; i <= n; i++) {
    if (getDigitSum(i) === n) return true;
  }

  return false;
}

for (let i = 1; i <= maxNum; i++) {
  if (!isSelfNumber(i)) console.log(i);
}
