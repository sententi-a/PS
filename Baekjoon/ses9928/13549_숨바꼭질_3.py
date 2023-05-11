# 숨바꼭질 3 https://www.acmicpc.net/problem/13549

"""
수빈 : 점 N
동생 : 점 K 

수빈이는 걷거나 순간이동을 할 수 있음
- 걷는다 : 1초 후 X-1 / X+1로 이동 
- 순간이동한다 : 0초 후 2 * X로 이동

수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초 후인지 구하기
"""

import sys
from math import ceil

sys.setrecursionlimit(10**9)

subin, sister = map(int, sys.stdin.readline().split())
max_pos = ceil(sister / subin) * subin

visited = [False for _ in range(max_pos+1)]
visited[subin] = True
candidates = []
stack = [(subin, 0)] # (pos, time_passed)

def check_pos(x, max_pos, sister):
    answer = []

    if 0 <= x - 1 <= max_pos:
        answer.append(x-1)
    
    # 현재 위치가 동생 위치보다 오른쪽이라면 왼쪽으로 가야 함
    if x > sister:
        return answer

    if 0 <= x + 1 <= max_pos:
        answer.append(x+1)
    
    if 0 < 2 * x <= max_pos:
        answer.append(2 * x)
    
    return answer
        
def dfs(curr, time, goal):
    global max_pos

    if candidates and min(candidates) < time:
        return
    
    # 목표 지점에 도달했을 때
    if curr == goal:
        candidates.append(time)
        return
    
    for pos in check_pos(curr, max_pos, goal):
        if not visited[pos]:
            if pos == 2 * curr:
                new_time = time
            else:
                new_time = time + 1

            visited[pos] = True
            dfs(pos, new_time, goal)
            visited[pos] = False

dfs(subin, 0, sister)


# print(candidates)
print(min(candidates))