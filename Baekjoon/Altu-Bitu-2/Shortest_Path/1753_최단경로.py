# 최단경로 https://www.acmicpc.net/problem/1753

import sys
from heapq import heappush, heappop

INF = 10 * 300000 + 1

vertex, edge = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

dists = [INF for _ in range(vertex + 1)]
dists[start] = 0

graph = [[] for _ in range(vertex + 1)]

for _ in range(edge):
    v1, v2, cost = map(int, sys.stdin.readline().split())

    graph[v1].append((cost, v2))

heap = [(0, start)]

while heap:
    c, v = heappop(heap)

    if dists[v] < c:
        continue

    for distance, adj in graph[v]:
        if dists[adj] > c + distance:
            dists[adj] = c + distance
            heappush(heap, (dists[adj], adj))

for i in range(1, vertex + 1):
    if dists[i] == INF:
        print("INF")
        continue
    print(dists[i])
