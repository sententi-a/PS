# 기숙사 바닥 https://www.acmicpc.net/problem/2858

"""
상근이 방의 크기는 L*W
자신의 방도 1*1 크기 타일로 채우려고 함 
가장자리는 빨간색으로, 나머지는 갈색으로 채우려고 함

빨간색과 갈색 타일의 개수가 주어졌을 때, 상근이 방의 크기를 구하기
큰 수가 L, 작은 수가 W
"""

import sys

red, brown = map(int, sys.stdin.readline().split())


"""
red + brown =  L * W - Brown 
brown = a * b
L = a + 2
W = b + 2
"""


def check(inner_width: int, inner_height: int, red: int, brown: int):
    """
    brown의 가로, 세로 길이, 빨간색 타일 개수, 갈색 타일 개수가 주어졌을 때
    빨간색 타일이 가장자리, 나머지가 갈색인 타일 배치가 가능한지 리턴하는 함수
    """

    if (inner_height + 2) * (inner_width + 2) == red + brown:
        return True

    return False


for inner_height in range(1, int(brown**0.5) + 1):
    if brown % inner_height == 0:
        inner_width = brown // inner_height

        if check(inner_width, inner_height, red, brown):
            print(inner_width + 2, inner_height + 2)
            break
