# 최솟값 찾기 https://www.acmicpc.net/problem/11003

'''
N개의 수 A_1, A_2, ... A_N과 L이 주어짐
D_i = A_(i-L+1) ~ A_i 중 최솟값이라고 할 때, D에 저장된 수를 출력
이 때 i<=0 인 A_i는 무시하고 D를 구해야 함
'''

import sys
from collections import deque

n, l = map(int, sys.stdin.readline()) #n개의 수, 최솟값 찾기 위한 변수
nums = list(map(int, sys.stdin.readline().split()))
deq = deque(nums)
answers = [min(deq) for _ in range(n)]

for i in range(n):
    