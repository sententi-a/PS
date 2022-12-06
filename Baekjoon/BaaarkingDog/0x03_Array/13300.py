# 방 배정 https://www.acmicpc.net/problem/13300

"""
1학년부터 6학년까지 학생들이 묵을 방을 배정
동성끼리, 같은 학년끼리 배정 (한 방에 한 명 배정도 가능)
한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때, 
조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수 구하기
s(성별) : 0(여), 1(남) / y(학년) : 1 ~ 6
"""
from math import ceil 

n, k = map(int, input().split())

girls = []
boys = []

room = 0 # 필요한 방의 개수 

for _ in range(n):
    s, y = map(int, input().split())
    if s == 0:
        girls.append(y)
    else:
        boys.append(y)


for i in range(1, 7):
    g_count = girls.count(i)
    b_count = boys.count(i)

    room += ceil(g_count / k) + ceil(b_count / k)


print(room)