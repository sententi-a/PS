# 로또 https://acmicpc.net/problem/6603

"""
49가지 수 중 k개의 수를 골라 집합 S를 만든 다음, 그 수만 가지고 번호를 선택
집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 출력하기 
- 입력의 마지막 줄에는 0이 하나 주어짐
- 수를 고르는 모든 방법을 사전 순으로 출력하기
"""

import sys

def sol(cur):
    if cur == 6:
        # answer.append(" ".join(map(str, tmp)))
        print(*tmp[:6], sep=" ")
        return

    for i in range(len(numbers)):
        tmp[cur] = numbers[i]
        if not used[i] and tmp[cur] > tmp[cur-1]:
            used[i] = True
            sol(cur+1)
            used[i] = False


answer = []

while(1):
    case = list(map(int, sys.stdin.readline().split()))

    if case[0] == 0:
        # break
        exit()
    # 0 입력시 종료

    k, numbers = case[0], case[1:]
    used = [False for _ in range(k)]
    tmp = [0] * 7

    sol(0)
    print(" ")

