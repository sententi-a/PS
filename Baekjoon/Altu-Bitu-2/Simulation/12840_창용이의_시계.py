# 창용이의 시계 https://www.acmicpc.net/problem/12840

"""
현재 시간이 주어지고, n개의 쿼리가 주어졌을 때 시계가 기리키는 시간 출력
1) T == 1 : 시계를 앞으로 c초 돌림
2) T == 2 : 시계를 뒤로 c초 돌림 
3) T == 3 : 창용이가 조작한 시계의 상황 출력
"""

import sys

hour, minute, second = map(int, sys.stdin.readline().split())
clock = (hour * 3600) + (minute * 60) + second

query_count = int(sys.stdin.readline())

for _ in range(query_count):
    _input = sys.stdin.readline()


    if int(_input[0]) == 3: 
        s = clock % 60
        m = (clock % 3600) // 60
        h = clock // 3600

        print(h, m, s)
    
    else:
        query, seconds_control = map(int, _input.rstrip().split())
        # seconds_control초만큼 앞으로 돌리기
        if query == 1:
            clock = (clock + seconds_control) % (24 * 3600)
        else:
            # 파이썬의 모듈러 연산 (-4) % 10 => 6 
            clock = (clock - seconds_control) % (24 * 3600)


        