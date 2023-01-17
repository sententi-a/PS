# 숨바꼭질 https://www.acmicpc.net/problem/1697

"""
수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동
순간이동을 하는 경우 1초 후에 2*X 위치로 이동

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하기
"""

import sys
from collections import deque


subin, sister = map(int, sys.stdin.readline().split())

# 둘의 시작 위치가 같다면
if subin == sister:
    print(0)
    exit()

visited = [0 for _ in range(100001)]
visited[sister] = -1 # 동생의 위치 

queue = deque([subin])
result = 0

def move(x, dx):
    if 0 <= dx < 100001:
        # 동생이 있는 곳이면
        if visited[dx] == -1:
            print(visited[x] + 1)
            exit()
        # 아직 방문하지 않은 좌표라면
        elif visited[dx] == 0:
            visited[dx] = visited[x] + 1
            queue.append(dx)


while queue:
    x = queue.popleft()

    left = x - 1
    right = x + 1
    jump = x << 1


    move(x, left)
    move(x, right)
    move(x, jump)
     