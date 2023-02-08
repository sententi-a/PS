# N과 M (6) https://acmicpc.net/problem/15655
"""
N개의 자연수와 자연수 M이 주어졌을 때, 조건을 만족하는 길이가 M인 수열 모두 구하기
N개의 자연수는 모두 다른 수
- N개의 자연수 중 M개를 고른 수열
- 고른 수열은 오름차순 
- 수열은 사전 순으로 증가하는 순서로 출력해야 함 
예) 1 7, 1 8, 1 9, 7 1, 7 8, 7 9...
"""

import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
answers = [0 for _ in range(m+1)]
used = [False for _ in range(n)]

numbers.sort()

def sol(cur):
    global n, m

    if cur == m:
        print(*answers[:m], sep=" ")
        return

    for i in range(n):
        answers[cur] = numbers[i]
        
        if not used[i] and answers[cur-1] < answers[cur]:
            used[i] = True
            sol(cur+1)
            used[i] = False

sol(0)