# 암기왕 https://www.acmicpc.net/problem/2776

"""
수첩 1 : 연종이가 하루 동안 본 정수들
수첩 2 : 동규가 질문한 정수들 
수첩 2에 적혀있는 순서대로, 수첩 1에 있으면 1을, 없으면 0을 출력
"""

import sys 
# from collections import defaultdict

tc = int(sys.stdin.readline())

for _ in range(tc):
    num_cnt_in_note1 = int(sys.stdin.readline())
    note1 = set(list(map(int, sys.stdin.readline().split())))
    num_cnt_in_note2 = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))

    for num in note2: 
        if num in note1: 
            print(1)
        else:
            print(0)
