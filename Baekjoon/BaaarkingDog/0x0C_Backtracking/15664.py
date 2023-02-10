# N과 M (10) https://acmicpc.net/problem/15664

"""
N개의 자연수와 자연수 M이 주어졌을 때, 조건 만족하는 길이가 M인 수열 모두 구하기
- N개의 자연수 중 M개를 고른 수열
- 고른 수열은 비내림차순
- 중복되는 수열을 여러 번 출력하면 안 됨
- 수열은 사전 순으로 증가하는 순서로 출력
"""

import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
used = [False for _ in range(n)]

tmp = [0 for _ in range(m+1)]
answers = []

def sol(cur):
    global n, m

    if cur == m:
        answers.append(" ".join(map(str, tmp[:m])))
        return

    for i in range(n):
        tmp[cur] = numbers[i]
        if tmp[cur] >= tmp[cur-1] and not used[i]:
            used[i] = True
            sol(cur+1)
            used[i] = False


sol(0)
result = dict.fromkeys(answers)
print(*result, sep="\n")