# 공약수 https://www.acmicpc.net/problem/2436

"""
두 개의 자연수가 주어졌을 때, 이 두 수를 최대공약수와 최소공배수로 하는 두 개의 자연수를 구하기
- 이런 자연수가 여러 쌍이 있을 때, 두 자연수의 합이 최소가 되는 두 수를 출력
"""

import sys

gcm, lcm = map(int, sys.stdin.readline().split())

if gcm == lcm:
    print(gcm, gcm)
    exit()

# A * B = gcm * lcm
# lcm / gcm = a * b(a, b 서로소)


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


divided = lcm // gcm
answer = [0, 0]

for i in range(1, int(divided**0.5) + 1):
    if divided % i == 0:
        a, b = divided // i, i

        if gcd(a, b) == 1:
            answer[0], answer[1] = gcm * b, gcm * a

print(answer[0], answer[1])
