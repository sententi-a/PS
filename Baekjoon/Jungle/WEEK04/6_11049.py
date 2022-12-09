# 행렬 곱셈 순서 https://www.acmicpc.net/problem/11049

import sys 

n = int(sys.stdin.readline()) # 행렬의 개수

matrix = []
table = [[0 for _ in range(n)] for _ in range(n)] # table[i][j] : i~j번째 행렬을 곱하는 연산 횟수 최솟값

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for gap in range(1, n): # gap (서로 곱하는 행렬 사이에 몇 개의 행렬이 더 있는가)
    for i in range(n - gap): # table 2차원 행렬의 행 값 
        j = i + gap # 2차원 행렬 table의 열 값

        if gap == 1:
            table[i][j] = matrix[i][0] * matrix[i][1] * matrix[j][1]
            continue

        table[i][j] = 2 ** 32

        for k in range(i, j):
            table[i][j] = min(table[i][j], table[i][k] + table[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])

print(table[0][n-1])