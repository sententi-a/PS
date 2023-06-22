# 여행 가자 https://www.acmicpc.net/problem/1976

"""
도시 N개가 있고, 임의의 두 도시 사이에 길이 있을 수도, 없을 수도 있음
여행 일정이 주어졌을 때 이 여행 경로가 가능한지 알아보기 
- 중간에 다른 도시를 경유할 수 있음
- 같은 도시를 여러 번 방문하는 것도 가능 
"""

import sys

def find_root_parent(parent: list, node: int):
    if parent[node] == node:
        return node
    else:
        return find_root_parent(parent, parent[node])


city_cnt = int(sys.stdin.readline())
visit_cnt = int(sys.stdin.readline())

graph = []

for _ in range(city_cnt):
    graph.append(list(map(int, sys.stdin.readline().split())))

plan = list(map(int, sys.stdin.readline().split()))

parent = [i for i in range(city_cnt)]

# 조상 노드 구하기 (숫자가 작은 쪽이 더 위계가 높음)
for i in range(city_cnt):
    for j in range(city_cnt):
        if graph[i][j] == 1:
            a = find_root_parent(parent, i)
            b = find_root_parent(parent, j)

            if a > b:
                parent[a] = b
            else:
                parent[b] = a

# 여행 계획을 선형적으로 탐색하면서 공통 조상 구함
# 공통 조상이 다르다면 두 노드는 어떤 경로로든 이어지지 않았다는 뜻이므로 NO를 출력
for i in range(1, visit_cnt):
    if not find_root_parent(parent, plan[i-1] - 1) == find_root_parent(parent, plan[i] - 1):
        print('NO')
        exit()
    
print('YES')
