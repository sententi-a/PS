# 서로 다른 부분 문자열의 개수 https://www.acmicpc.net/problem/11478

"""
문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램
(EX) ababc => a, b, c, ab, ba, bc, aba, bab, abc, abab, babc, ababc
"""

import sys

string = sys.stdin.readline().rstrip()
substring = set()

for gap in range(1, len(string)+1):
    for start in range(len(string)):
        target = start
        while target < len(string):
            substring.add(string[start:target+gap])
            target += gap

print(len(substring))