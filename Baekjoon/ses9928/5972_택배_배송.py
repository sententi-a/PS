# 택배 배송 https://www.acmicpc.net/problem/5972

"""
현서가 찬홍이에게 가는 길에 만나는 모든 소들에게 여물을 줘야 함
N개의 헛간과, M개의 소가 다니는 길(양방향)이 있고 각각의 길은 C_i 마리의 소가 있음 
소들의 길은 두 개의 떨어진 헛간인 A_i와 B_i를 이음
농부 현서는 헛간 1에 있고 찬홍이는 헛간 N에 있음
길을 지나가는 소의 수가 주어질 때 찬홍이에게 가는 길에 줘야할 최소 여물은 얼마일까?
"""

import sys 
from heapq import heappush, heappop

INF = sys.maxsize

# node, edge
shed, cow_road = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(shed + 1)] # graph[i] == (cows, adjacent)
dist = [INF for _ in range(shed + 1)]

for _ in range(cow_road):
    shed1, shed2, cows = map(int, sys.stdin.readline().split())

    graph[shed1].append((cows, shed2))
    graph[shed2].append((cows, shed1))


def dijkstra(start: int, dist: list):
    # (cows, node)
    heap = [(0, start)]
    dist[start] = 0

    while heap:
        cost, curr = heappop(heap)

        # 이미 최단거리가 구해진 노드라면 패스
        if dist[curr] < cost:
            continue

        for cows, adj in graph[curr]:

            if dist[adj] >  cost + cows:
                dist[adj] = cost + cows
                heappush(heap, (dist[adj], adj))

dijkstra(1, dist)
print(dist[shed])