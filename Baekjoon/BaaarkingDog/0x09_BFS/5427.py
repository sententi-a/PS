# 불 https://acmicpc.net/problem/5427

"""
매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼짐 
상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없음
상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있음
상근이가 얼마나 빨리 빌딩을 탈출할 수 있는지 구하기
. : 빈 공간
# : 벽
@ : 상근이의 시작 위치
* : 불
"""
from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global q, f
    while q:
        temp = deque()
        while q:
            x, y = q.popleft()
            if (x == h - 1 or y == w - 1 or x == 0 or y == 0) and s[x][y] != "*": return s[x][y]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == "." and s[x][y] != "*":
                    s[nx][ny] = s[x][y] + 1
                    temp.append([nx, ny])
        q = temp
        temp = deque()

        while f:
            x, y = f.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == 0 and s[nx][ny] != "#":
                    s[nx][ny] = "*"
                    visit[nx][ny] = 1
                    temp.append([nx, ny])
        f = temp
        
t = int(input())

for i in range(t):
    w, h = map(int, input().split())
    s, f, q = [], deque(), deque()
    visit = [[0] * w for i in range(h)]

    for j in range(h):
        a = list(input().strip())
        s.append(a)

        for k in range(w):
            if a[k] == "@":
                s[j][k] = 0
                q.append([j, k])
            elif a[k] == "*":
                f.append([j, k])
                visit[j][k] = 1
    result = bfs()
    print(result + 1 if result != None else "IMPOSSIBLE")


# import sys
# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for _ in range(int(sys.stdin.readline())):
#     building = []
#     queue = deque()
#     answer = 0
#     done = False

#     row, col = map(int, sys.stdin.readline().split())

#     f_visited = [[0 for _ in range(row)] for _ in range(col)]
#     s_visited = [[0 for _ in range(row)] for _ in range(col)]

#     for i in range(col):
#         building.append(list(map(str, sys.stdin.readline().rstrip())))
#         for j in range(row):
#             # 불일 경우 
#             if building[i][j] == '*':
#                 queue.append(('*', i, j))
#                 f_visited[i][j] = 1
#             # 상근이일 경우
#             elif building[i][j] == '@':
#                 queue.append(('@', i, j))
#                 s_visited[i][j] = 1
    
#     while queue:
#         flag, x, y = queue.popleft()
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]

                
#             if 0 <= nx < col and 0 <= ny < row:
#                 # 불 이동
#                 if flag == '*':
#                     if f_visited[nx][ny] == 0 and building[nx][ny] != '#':
#                         if building[nx][ny] == '@':
#                             done = True
#                             break
#                         queue.append(('*', nx, ny))
#                         f_visited[nx][ny] = f_visited[x][y] + 1
#                         building[nx][ny] = '*'
                
#                 # 상근 이동
#                 elif flag == '@':
#                     if s_visited[nx][ny] == 0 and building[nx][ny] == '.':
#                         queue.append(('@', nx, ny))
#                         s_visited[nx][ny] = s_visited[x][y] + 1
#                         building[nx][ny] = '@'
#                         building[x][y] = '.'

#             # 상근이가 탈출했을 경우
#             else:
#                 if flag == '@':
#                     answer = s_visited[x][y]
#                     # answer = count 
#                     done = True
#                     break
            
#             if done:
#                 break
    
#         if done:
#             break

#     if answer:
#         print(answer)
#         continue
#     else:
#         print("IMPOSSIBLE")
#         continue