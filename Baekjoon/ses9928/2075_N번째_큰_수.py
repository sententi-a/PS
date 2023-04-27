# N번째 큰 수 https://www.acmicpc.net/problem/2075

"""
N*N의 표에 수 N^2개가 채워져 있고, 
모든 수는 자신의 한 칸 위에 있는 수보다 큼

이 때 N번째 큰 수를 찾는 프로그램 작성하기
1<=N<=1500 
"""

import sys 
from heapq import heappop, heappush

n = int(sys.stdin.readline())
numbers = []

for _ in range(n): 
    row = list(map(int, sys.stdin.readline().split()))
    
    for num in row:
        if len(numbers) < n:
            heappush(numbers, num)
        else: 
            heappop(numbers)
            heappush(numbers, num)

print(heappop(numbers))