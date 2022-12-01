# 동전 https://www.acmicpc.net/problem/9084
# 동전의 종류가 주어질 때 주어진 금액을 만드는 모든 방법을 세는 프로그램
# 순서는 고려하지 않음 

import sys

T = int(sys.stdin.readline()) # 테스트 케이스 개수 

for _ in range(T):
    N = int(sys.stdin.readline()) # 동전의 가짓수 
    coins = list(map(int, sys.stdin.readline().split())) # 동전 종류
    goal = int(sys.stdin.readline()) # 만들어야 할 금액
 
    table = [0 for _ in range(goal + 1)]
    table[0] = 1
    
    for coin in coins:
        for i in range(coin, goal + 1):
            table[i] += (table[i - coin]) # 만약에 2, 3, 5원으로 5원을 만든다고 하면 table[2]가 1이고 table[5]는 2+3이므로 table[5] += table[5-3]가 됨 

    print(table[goal])