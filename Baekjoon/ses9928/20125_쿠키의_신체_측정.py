# 쿠키의 신체 측정 https://www.acmicpc.net/problem/20125

"""
한 변의 길이가 N인 정사각형 판 위에 누워있는 쿠키의 신체 측정
- 판의 맨 왼쪽 위 칸을 (1, 1)로 함 

쿠키의 신체가 주어졌을 때 심장의 위치, 팔, 다리, 허리의 길이 구하기
"""

import sys 

n = int(sys.stdin.readline()) 

body = []

for i in range(n):
    body.append(list(sys.stdin.readline().rstrip()))
    

# 머리 구하기
head = 0

for i in range(n):
    for j in range(n):
        if body[i][j] == '*':
            head = (i, j)
            break
    if head:
        break

# 양쪽 팔 구하기
left_arm, right_arm = 0, 0

for j in range(n):
    if body[head[0] + 1][j] == '*':
        left_arm = head[1] - j
        break

for j in range(n-1, -1, -1):
    if body[head[0] + 1][j] == '*':
        right_arm = j - head[1]
        break

# 허리 구하기
back = 0

for i in range(head[0] + 2, n):
    if body[i][head[1]] == '*':
        back += 1
    else:
        break

# 양쪽 다리 구하기
left_leg, right_leg = 0, 0

for i in range(head[0] + back + 2, n):
    # 왼쪽 다리 
    if body[i][head[1]-1] == '*':
        left_leg += 1
    # 오른쪽 다리 
    if body[i][head[1]+1] == '*':
        right_leg += 1
    # 다리 계산 끝났을 경우 
    if body[i][head[1]-1] != '*' and body[i][head[1]+1] != '*':
        break
    

print(head[0] + 2, head[1] + 1)
print(left_arm, right_arm, back, left_leg, right_leg)