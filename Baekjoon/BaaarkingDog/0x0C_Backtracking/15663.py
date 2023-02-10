# N과 M (9) https://acmicpc.net/problem/15663
"""
N개의 자연수와 자연수 M이 주어졌을 때, 조건을 만족하는 길이가 M인 수열 모두 구하기
- N개의 자연수 중 M개를 고른 수열
- ** 중복되는 수열을 여러 번 출력하면 안 됨
- 수열은 사전 순으로 증가하는 순서로 출력 
예제 입력 : 3 1 \n4 4 2
예제 출력 : 2 \n4
"""

import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
used = [False for _ in range(n)]
tmp = [0 for _ in range(m+1)]
answers = []

numbers.sort()

def sol(cur):
    global n, m

    if cur == m:
        # print(*tmp[:m])
        # set의 원소는 해시할 수 있는 immutable한 값이어야 함(str, int, tuple)
        answers.append(" ".join(map(str, tmp[:m])))
        return 

    for i in range(n):
        if not used[i]:
            tmp[cur] = numbers[i]
            used[i] = True
            sol(cur+1)
            used[i] = False


sol(0)
# answers.sort()
result = dict.fromkeys(answers)
# result.
print(*result, sep="\n")
