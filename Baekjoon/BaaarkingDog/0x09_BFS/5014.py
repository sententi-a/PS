# 스타트링크 https://acmicpc.net/problem/5014

"""
스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고,
스타트링크가 있는 곳의 위치는 G층
강호가 지금 있는 곳은 S층이고, 엘리베이터를 타고 G층으로 이동하려고 함

강호가 탄 엘리베이터는 버튼이 2개밖에 없음 
U : 위로 U층을 가는 버튼
D : 아래로 D층을 가는 버튼 
(만약 U층 위, D층 아래에 해당하는 층이 없을시 엘리베이터는 움직이지 않음)

강호가 G층에 도착하려면 버튼을 적어도 몇 번 눌러야 하는지 출력
만약 엘리베이터를 이용해서 G층에 갈 수 없다면 "use the stairs" 출력

건물은 1층부터 시작함
"""

import sys
from collections import deque

# F(건물 총 층 수), S(현재 강호 층), G(스타트링크 층), U(위 버튼), D(아래 버튼)
total, curr, goal, up, down = map(int, sys.stdin.readline().split())

queue = deque([curr]) # 강호가 이동할 곳을 담는 큐
visited = [0 for _ in range(total + 1)] # 0은 padding, 1~total
visited[curr] = 1

# 현재 강호가 있는 층과 가려고 하는 층이 같다면
if curr == goal:
    print(0)
    exit()

def move(x, dx):
    global total, goal
    # 스타트링크 층에 도달했다면
    if dx == goal:
        print(visited[x])
        exit()

    if 1 <= dx <= total:
        if visited[dx] == 0:
            queue.append(dx)
            visited[dx] += visited[x] + 1

while queue: 
    floor = queue.popleft()
    # 두 가지 경우를 경쟁 (큐에서 pop할 때마다 위로 올라가는 경우, 아래로 내려가는 경우 동시 비교)
    # 위로 올라가든, 아래로 내려가든 어차피 먼저 도달하면 그 때 출력 및 종료됨
    move(floor, floor + up)
    move(floor, floor - down)
    

print("use the stairs")