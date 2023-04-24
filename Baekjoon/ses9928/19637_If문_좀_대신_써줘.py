# IF문 좀 대신 써줘 https://www.acmicpc.net/problem/19637

"""
캐릭터가 가진 전투력을 기준으로 칭호를 붙여줌
10,000 이하 : WEAK
10,000 초과 - 100,000 이하 : NORMAL
10,000 초과 - 1,000,000 이하 : STRONG
"""

import sys 
from bisect import bisect_left

title_cnt, char_cnt = map(int, sys.stdin.readline().split())

titles = []
strengths = []

answers = []

idx = 0

for _ in range(title_cnt):
    _input = sys.stdin.readline().split()
    
    if not strengths or strengths[idx-1] != int(_input[1]):
        titles.append(_input[0])
        strengths.append(int(_input[1]))
        idx += 1

for _ in range(char_cnt):
    strength = int(sys.stdin.readline())
    pos = bisect_left(strengths, strength)
    answers.append(titles[pos])

print(*answers, sep="\n")    