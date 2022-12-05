# 두 수의 합 https://www.acmicpc.net/problem/3273

##### SUCCESS: 41620KB, 128ms #####
'''
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. 
ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
'''
import sys

n = int(sys.stdin.readline()) # 수열의 크기
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

x = int(sys.stdin.readline()) # a1 + a2 = x

count = 0 # a1 + a2를 만족하는 쌍의 수

front_p, rear_p = 0, len(nums)-1

while True:
    if front_p >= rear_p:
        break
    
    if nums[front_p] + nums[rear_p] < x:
        front_p += 1
    elif nums[front_p] + nums[rear_p] > x:
        rear_p -= 1
    else:
        count += 1
        front_p += 1
        rear_p -= 1

print(count)
