# GCD 합 https://www.acmicpc.net/problem/9613

"""
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD 합 구하기
"""

import sys 
from itertools import combinations

def get_gcd(a, b):
    if b > a:
        a, b = b, a

    while b > 0:
        rest = a % b
        a, b = b, rest

    return a

tc_cnt = int(sys.stdin.readline())

for _ in range(tc_cnt):
    answer = 0
    nums = list(map(int, sys.stdin.readline().split()))[1:]
    
    for comb in combinations(nums, 2):
        gcd = get_gcd(comb[0], comb[1])
        answer += gcd

    print(answer)