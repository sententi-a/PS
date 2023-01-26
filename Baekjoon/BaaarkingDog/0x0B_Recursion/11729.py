# 하노이 탑 이동 순서 https://acmicpc.net/problem/11729

"""
반경이 서로 다른 n개의 원판을 
첫 번째 장대에서 세 번째 장대로 옮길 때
이 작업을 수행하는데 필요한 이동 순서 출력 (이동 횟수는 최소)

- 한 번에 한 개의 원판만 옮김
- 쌓아놓은 원판은 항상 위의 것이 아래 것보다 작아야 함 
* 디스크가 n개일 때 이동 횟수는 2^n - 1
"""

import sys
 
disk = int(sys.stdin.readline()) # 원판의 수 
count = 0

def sol(n):
    print(2**n - 1)
    hanoi_path(n, 1, 3)
    return

def hanoi_path(n, start, end):

    if n == 1:
        print(start, end)
        return
    
    mid = 6 - (start + end)

    hanoi_path(n-1, start, mid)
    print(start, end)
    hanoi_path(n-1, mid, end)


sol(disk)