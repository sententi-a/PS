# 시리얼 번호 acmicpc.net/problem/1431

"""
기타를 시리얼 번호 순서대로 정렬
1. 번호가 짧은 것이 더 먼저 옴
2. 길이가 같다면, 모든 자리수(숫자)의 합이 더 작은 게 먼저 옴 
3. 사전순 (숫자가 알파벳보다 사전순으로 작음)
"""

import sys

count = int(sys.stdin.readline())

guitars = [sys.stdin.readline().rstrip() for _ in range(count)]

def digit_sum(serial_num):
    result = 0
    for each in serial_num:
        if each.isdigit():
            result += int(each)
    # print(result)
    return result

guitars.sort(key=lambda x: (len(x), digit_sum(x), x))

print(*guitars, sep="\n")