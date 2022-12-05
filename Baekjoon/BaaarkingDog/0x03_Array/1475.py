# 방번호 https://acmicpc.net/problem/1475

import sys
room_num = sys.stdin.readline().rstrip()

answer = [0 for _ in range(10)]

# 6이나 9가 나오면 answer[6], answer[9] 중 더 작은 값을 가지는 인덱스의 요소 값을 + 1
for i in range(len(room_num)):
    if room_num[i] == '6' or room_num[i] == '9':
        if answer[6] < answer[9]:
            answer[6] += 1
        else:
            answer[9] += 1
    else:
        answer[int(room_num[i])] += 1

print(max(answer))