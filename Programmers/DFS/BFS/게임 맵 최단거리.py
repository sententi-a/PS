from collections import deque 

def solution(maps):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps)) ]
    
    queue = deque([(0, 0)])
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        # print(x, y)
        
        if x == len(maps) - 1 and y == len(maps[0])-1:
            answer = maps[x][y]
            return answer
            
        # visited[x][y] = True
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if not visited[nx][ny] and maps[nx][ny] != 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
    
    answer = -1
    print(answer)
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])