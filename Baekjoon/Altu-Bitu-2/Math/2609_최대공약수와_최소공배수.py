# 최대공약수와 최소공배수 https://www.acmicpc.net/problem/2609

import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(num1, num2):

    while num2 > 0:
        rest = num1 % num2
        num1, num2 = num2, rest
    
    return num1


if a > b:
    gcd_num = gcd(a, b)
else:
    gcd_num  = gcd(b, a)


print(gcd_num)
print(a * b // gcd_num)