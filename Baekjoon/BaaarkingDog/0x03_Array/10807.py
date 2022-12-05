# 개수 세기 https://acmicpc.net/problem/10807

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

count = 0 # the number of [v]s in nums list

###### 1st : using for loop (30850KB, 72ms) ######
for num in nums:
    if num == v:
        count += 1

print(count)

###### 2nd : using .count() (30850KB, 68ms) ######
#print(nums.count(v))