# 백대열 https://www.acmicpc.net/problem/14490

import sys

def get_gcd(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        rest = a % b
        a, b = b, rest

    return a 

num1, num2 = map(int, sys.stdin.readline().split(':'))

gcd = get_gcd(num1, num2)

print(f'{num1//gcd}:{num2//gcd}')