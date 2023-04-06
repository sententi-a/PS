# 에라토스테네스의 체 https://www.acmicpc.net/problem/2960

"""
2부터 n까지 모든 정수를 적음 
아직 지우지 않은 수 중 가장 작은 수 P (소수)를 찾음
P를 지우고, 아직 지우지 않은 P의 배수를 차례로 지움 

n, k가 주어졌을 때 k번째 지우는 수 구하기 
"""

import sys 

n, k = map(int, sys.stdin.readline().split())

count = 0

is_prime_num = [True for _ in range(n+1)]
is_prime_num[0], is_prime_num[1] = False, False

for i in range(2, n+1):
        for j in range(i, n+1, i):
            if is_prime_num[j]:
                count += 1
                is_prime_num[j] = False

                if count == k:
                    print(j)
                    exit()

        
