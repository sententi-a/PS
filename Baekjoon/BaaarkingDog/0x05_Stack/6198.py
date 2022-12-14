# 옥상 정원 꾸미기 https://www.acmicpc.net/problem/6198

########################33904KB	104ms############################

"""
i번째 빌딩의 키가 hi이고, 모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다.
i번째 빌딩 관리인이 볼 수 있는 다른 빌딩의 옥상 정원은 i+1, i+2, .... , N이다.
그런데 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 그 다음에 있는 모든 빌딩의 옥상은 보지 못한다.
각 관리인들이 벤치마킹이 가능한 빌딩의 수의 합을 출력하라.
"""

import sys

buildings = []
for i in range(int(sys.stdin.readline())): 
    buildings.append(int(sys.stdin.readline()))

stack = []
count = 0

for building in buildings: 

  while stack and stack[-1] <= building: #현재 보고 있는 건물이 stack의 마지막 건물보다 크거나 같으면 막힘
    stack.pop()

  stack.append(building)
  count += len(stack)-1

print(count)