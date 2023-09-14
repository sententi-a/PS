# N과 M (9) https://www.acmicpc.net/problem/15663

"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램 작성
- N개의 자연수 중 M개를 고른 수열 
- 중복되는 수열을 여러 번 출력하면 안 됨 
- 수열은 사전 순으로 증가하는 순서로 출력 
"""

import sys


n, m = map(int, sys.stdin.readline().split())
# 오름차순으로 출력하기 위함
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

answer = set()
visited = [False for _ in range(len(nums))]
temp = [0 for _ in range(m)]


def backtracking(k):
    global n, m

    if k == m:
        answer.add(" ".join(map(str, temp)))
        # answer.add(temp)
        return

    for i in range(n):
        if not visited[i]:
            temp[k] = nums[i]
            visited[i] = True
            backtracking(k + 1)
            visited[i] = False


backtracking(0)

result = dict.fromkeys(answer)
print(*result, sep="\n")
