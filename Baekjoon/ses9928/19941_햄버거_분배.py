# 햄버거 분배 https://www.acmicpc.net/problem/19941

import sys 

"""
사람들은 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있음
햄버거를 먹을 수 있는 사람의 최대 수 구하기 
"""

table, dist = map(int, sys.stdin.readline().split())
info = sys.stdin.readline().rstrip()

ate = [False for i in range(table)]

cnt = 0 

for i in range(table):
    if info[i] == 'P':
        found = False
        # 더 많은 사람이 먹을 수 있게 앞쪽의 먼 곳부터 탐색
        for j in range(dist, 0, -1):
            if i - j >= 0:
                if info[i - j] == 'H' and not ate[i - j]:
                    ate[i - j] = True
                    cnt += 1
                    found = True
                    break
        if found:
            continue

        # 앞쪽에서 못 찾으면, 뒤에서 찾음
        for j in range(1, dist+1):
            if i + j < table:
                if info[i + j] == 'H' and not ate[i + j]:
                    ate[i + j] = True
                    cnt += 1
                    break

print(cnt) 