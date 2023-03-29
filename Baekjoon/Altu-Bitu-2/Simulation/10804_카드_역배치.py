# 카드 역배치 https://www.acmicpc.net/problem/10804
"""
1-20까지 오름차순으로 놓인 카드들에 대해
입력으로 주어진 10개의 구간 순서대로 뒤집는 작업을 했을 때
마지막 카드들의 배치를 한 줄에 출력하기
"""

import sys

cards = [i for i in range(1, 21)]
temp = cards[:]

for _ in range(10):
    start, end = map(int, sys.stdin.readline().split())
    slice_list = temp[start-1:end]
    result = temp[:start-1] + slice_list[::-1] + temp[end:]
    temp = result[:]
    
    if _ == 9:
        print(*result)