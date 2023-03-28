// 덩치 https://www.acmicpc.net/problem/7568
// 몸무게, 키 모두 상대보다 커야 덩치가 크다
// 1st try : 일단 몸무게, 몸무게가 같으면 키 내림차순으로 정렬하고,
// 바로 앞 원소랑 비교했을 때 앞 원소가 덩치가 더 크면 반복문 내에서 몇 번째 순서인지를 answer로,
// 아니라면 이전 원소와 같은 rank를 넣음 -> 틀림 (weight 혹은 height가 같을 때 i-2, i-3 ... 계속 비교해야할수도)
//

const path = process.platform === "linux" ? "/dev/stdin" : "Baekjoon/7568.txt";
const fs = require("fs");
const input = fs.readFileSync(path).toString().trim().split("\n");

const people = parseInt(input[0]);
let bodyInfo = input.slice(1);

const answer = Array(people).fill(1); // 덩치 등수

bodyInfo = bodyInfo.map((elem, index) => {
  const [weight, height] = elem.split(" ").map((elem) => parseInt(elem));

  return { index, weight, height };
});

// bodyInfo.push({ index: -1, weight: 201, height: 201 });

// bodyInfo.sort((a, b) => {
//   if (b.weight !== a.weight) return b.weight - a.weight;
//   else return b.height - a.height;
// });

// let rank = 0;
// 나보다 앞에 있는 원소의 height 가 더 크면 index
// for (let i = 1; i <= people; i++) {
//   if (
//     bodyInfo[i - 1].height > bodyInfo[i].height &&
//     bodyInfo[i - 1].weight > bodyInfo[i].weight
//   ) {
//     answer[bodyInfo[i].index] = i;
//     rank = i;
//   } else {
//     answer[bodyInfo[i].index] = rank;
//   }
// }
// console.log(bodyInfo);

// bodyInfo.forEach((elem, index) => {
//   let count = 0;
//   for (let i = 0; i < people; i++) {
//     if (i === index) continue;
//     if (bodyInfo[i].weight > elem.weight && bodyInfo[i].height > elem.height) {
//       count++;
//     }
//   }
//   answer[index] = count + 1;
// });

console.log(answer.join(" "));
