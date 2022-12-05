# 평범한 배낭 https://www.acmicpc.net/problem/12865

import sys

n, k = map(int, sys.stdin.readline().split()) # 물품의 수, 버틸 수 있는 무게

items = [[0]] # 물품 정보
for _ in range(n):
    items.append(list(map(int, sys.stdin.readline().split()))) # 물건 무게, 물건 가치 순서로 저장 

table = [[0 for _ in range(k+1)] for _ in range(n+1)] # table[i][j] : i는 아이템, j는 배낭 무게

for i in range(1, n+1):
    weight, value = items[i]

    for j in range(1, k+1):
        table[i][j] = table[i-1][j] # 일단 지금 아이템을 선택하지 않았다고 간주
        if j >= weight and table[i-1][j-weight] + value > table[i][j]: # 만약 지금 아이템을 선택했을 때가 선택하지 않았을 때보다 가치가 더 크다면 선택
             table[i][j] = table[i-1][j-weight] + value

print(table[n][k])
