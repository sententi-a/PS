# 동전0 https://www.acmicpc.net/problem/11047

import sys

coins = [] # 동전 종류 담는 리스트
count = 0 # 사용하는 동전 개수 
n, k = map(int, sys.stdin.readline().split()) # 동전 종류, 목표 금액
goal = k

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

for i in range(n-1, -1, -1): # 가장 액수가 큰 동전부터 사용하는 방식으로 동전 개수 카운트
    if coins[i] <= goal :
        count += goal // coins[i]
        goal %= coins[i]

print(count)