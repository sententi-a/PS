# 중복 빼고 정렬하기 https://acmicpc.net/problem/10867

"""
N개의 정수가 주어졌을 때, 중복 없이 오름차순으로 정렬하기 
"""

import sys 

n = int(sys.stdin.readline())
dictionary = set(list(map(int, sys.stdin.readline().split())))

dictionary = sorted(list(dictionary))
print(*dictionary)