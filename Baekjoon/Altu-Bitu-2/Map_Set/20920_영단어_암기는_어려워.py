# 영단어 암기는 어려워 https://www.acmicpc.net/problem/20920

"""
정렬 우선순위
1. 자주 나오는 단어일수록 앞에 배치
2. 해당 단어의 길이가 길수록 앞에 배치
3. 사전순으로 배치

길이가 M 이상인 단어들만 외움 
중복 없음
"""

import sys
from collections import defaultdict


word_note = defaultdict(int)
word_cnt, length_limit = map(int, sys.stdin.readline().split())

for i in range(word_cnt):
    _input = sys.stdin.readline().rstrip() 
    if len(_input) >= length_limit:
        word_note[_input] += 1

result = list(word_note.items())
result.sort(key = lambda x: (-x[1], -len(x[0]), x[0]))

for key, value in result:
    print(key)