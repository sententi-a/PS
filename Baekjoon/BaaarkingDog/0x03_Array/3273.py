# 두 수의 합 https://www.acmicpc.net/problem/3273

##### using array : 47192KB	104ms #####
'''
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. 
ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
'''
import sys

n = int(sys.stdin.readline()) # 수열의 크기
nums = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline()) # a1 + a2 = x

count = 0
table = [0 for _ in range(x + 1)]

for num in nums:
    if num < x:
        table[num] = 1

for num in nums:
    if x % 2 == 0 and num == x / 2:
        continue
    if num < x and table[x-num] != 0:
        count += 1
        table[num], table[x-num] = 0, 0
    
print(count)