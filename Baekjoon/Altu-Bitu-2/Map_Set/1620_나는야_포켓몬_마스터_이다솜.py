# 나는야 포켓몬 마스터 이다솜 https://www.acmicpc.net/problem/1620

"""
포켓몬 도감에 기반해
포켓몬 번호를 입력하면 포켓몬 이름을 출력하고, 
포켓몬 이름을 입력하면 포켓몬 번호를 출력하기
"""

import sys
from collections import defaultdict

poketmon_cnt, problem_cnt = map(int, sys.stdin.readline().split())
num_dogam = defaultdict()
name_dogam = defaultdict()

for i in range(1, poketmon_cnt+1):
    num_dogam[i] = sys.stdin.readline().rstrip()
    name_dogam[num_dogam[i]] = i

for j in range(problem_cnt):
    _input = sys.stdin.readline().rstrip()
    if _input.isdigit():
        print(num_dogam[int(_input)])
    else:
        print(name_dogam[_input])