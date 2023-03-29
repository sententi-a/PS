# 알바생 강호 https://www.acmicpc.net/problem/1758
"""
8시가 되는 순간 손님들은 모두 입구에서 커피를 하나씩 받고, 자리 감
커피를 몇 번째 받는지에 따라 팁을 다른 액수로 줌 
원래 강호에게 주려고 생각했던 돈 - (받은 등수 - 1)만큼
-> 위의 식에서 음수가 나온다면, 팁을 받을 수 없음
"""

import sys

answer = 0
count = int(sys.stdin.readline())

tips = [int(sys.stdin.readline()) for _ in range(count)]
tips.sort(reverse=True)

for i in range(len(tips)):
    tip = tips[i]
    if tip - i < 0:
        break
    answer += tip - i

print(answer)