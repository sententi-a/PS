# 요세푸스 문제 https://www.acmicpc.net/problem/1158

##################### 30712KB 2056ms #############################

"""
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있을 때,
순서대로 K번째 사람을 제거한다고 하자. 
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속하고, 모두 제거될 때까지 계속된다.
이 때 (N, K) 요세푸스 순열을 구하는 프로그램을 작성하라.
(7,3) - <3, 6, 2, 7, 5, 1, 4>
"""

import sys

n, k = map(int, sys.stdin.readline().split())

prev = [i-1 for i in range(n+1)]
prev[1] = n
nxt = [i+1 for i in range(n+1)]
nxt[n] = 1

target = k
answer = []

for _ in range(n):
    answer.append(target)
    nxt[prev[target]] = nxt[target]
    prev[nxt[target]] = prev[target]
    for j in range(k):
        target = nxt[target]

print('<', end="")
print(*answer, sep=", ", end="")
print(">")