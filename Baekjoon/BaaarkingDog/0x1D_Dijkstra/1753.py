# 최단경로 https://www.acmicpc.net/problem/1753

import sys
from heapq import heappop, heappush

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

INF = sys.maxsize

graph = [[] for _ in range(V+1)]
dists = [INF for _ in range(V+1)]
dists[start] = 0

pq = []
heappush(pq, (0, start))

for _ in range(E):
    v1, v2, weight = map(int, sys.stdin.readline().split())
    graph[v1].append((v2, weight))

while pq:
    cost, vertex = heappop(pq)
    if dists[vertex] < cost:
        continue

    for pair in graph[vertex]:
        adj, w = pair 

        if cost + w < dists[adj]:
            dists[adj] = cost + w
            heappush(pq, (cost+w, adj))

for i in range(1, len(dists)):
    if dists[i] == INF:
        print('INF')
        continue
    print(dists[i])

