# 좌표 정렬하기 2 https://www.acmicpc.net/problem/11651

import sys

count = int(sys.stdin.readline())
coordinates = []

for _ in range(count):
    coordinates.append(tuple(map(int, sys.stdin.readline().split())))

coordinates.sort(key = lambda x: (x[1], x[0]))

for x, y in coordinates:
    print(x, y)