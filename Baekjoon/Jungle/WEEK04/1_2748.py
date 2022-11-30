# 피보나치 수 2 https://www.acmicpc.net/problem/2748

import sys 
n = int(sys.stdin.readline()) 

table = [0 for _ in range(n+1)] # 0~n번째 피보나치 수를 저장하기 위한 테이블 

table[0] = 0 
table[1] = 1

for i in range(2, n+1):
    table[i] = table[i-2] + table[i-1]

print(table[n]) 