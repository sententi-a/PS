# 파일 정리 https://www.acmicpc.net/problem/20291

"""
파일을 확장자 별로 정리해 몇 개씩 있는지 알려줘야 함
보기 편하게 확장자들을 사전 순으로 정렬해야 함
"""

import sys
from collections import defaultdict

file_cnt = int(sys.stdin.readline())
file_dict = defaultdict(int)

for i in range(file_cnt):
    file = sys.stdin.readline().rstrip()
    file_name, extension = file.split('.')

    file_dict[extension] += 1

sorted_dict = sorted(file_dict.items())

for key, value in sorted_dict:
    print(key, value)