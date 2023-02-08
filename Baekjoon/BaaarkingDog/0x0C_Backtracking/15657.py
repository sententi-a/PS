# N과 M (8) https://acmicpc.net/problem/15656
"""
N개의 자연수와 자연수 M이 주어졌을 때, 조건을 만족하는 길이가 M인 수열 모두 구하기
- N개의 자연수 중 M개를 고른 수열 (N개의 자연수는 모두 다른 수)
- 같은 수를 여러 번 골라도 됨 
- 고른 수열은 비내림차순
- 수열은 사전 순으로 증가하는 순서로 출력
"""
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

answers = [0 for _ in range(m+1)]

numbers.sort()

def sol(cur):
    global n, m

    if cur == m:
        print(*answers[:m], sep=" ")
        return

    for i in range(n):
        answers[cur] = numbers[i]

        if answers[cur-1] <= answers[cur]:
            sol(cur+1)
        
sol(0)