# 최소 스패닝 트리 https://www.acmicpc.net/problem/1197  
###### 크루스칼 알고리즘을 통해 해결

###### Union Find 알고리즘
def get_parent(parent: list, x: int):
    """부모 노드를 찾는 함수 """
    # 루트 노드가 아니라면 루트노드를 찾을 때까지 재귀적으로 호출 (1-3-7이 연결되어 있다면 7의 부모는 3이 아니라 1을 리턴할 수 있게)
    if parent[x] != x: 
        return get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent: list, a: int, b: int):
    """두 부모 노드를 합치는 함수 (더 작은 쪽으로 합치기)"""
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent: list, a, b):
    """같은 부모를 가지는지 확인"""
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return 1
    return 0

###### main
import sys

v, e = map(int, sys.stdin.readline().split()) # 정점 개수, 간선 개수
vertex = [i for i in range(v+1)] # 각 노드의 연결 상태를 나타내는 리스트 (인덱스값과 요소값이 같다면 연결되어 있지 않음)
edge = [] # 간선 정보를 담는 리스트 
weight = 0 # MST의 가중치 합

for _ in range(e):
    edge.append(tuple(map(int, sys.stdin.readline().split())))

edge.sort(key=lambda x:x[2]) # 간선의 가중치 값을 기준으로 오름차순 정렬

for i in range(e):
    a = get_parent(vertex, edge[i][0])
    b = get_parent(vertex, edge[i][1])
    if not find_parent(vertex, a, b): # 같은 그룹에 속하지 않으면 MST에 포함하고, 같은 그룹으로 합쳐줌
        weight += edge[i][2]
        union_parent(vertex, a, b)

print(weight)
