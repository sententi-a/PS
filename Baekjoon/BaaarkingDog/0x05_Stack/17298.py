# 오큰수 https://www.acmicpc.net/problem/17298

"""
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미함. 그러한 수가 없는 경우에 오큰수는 -1

A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1
A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1

총 N개의 수의 오큰수를 출력하시오. 
O(n) 선으로 끝내기
"""

import sys 

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

stack = []
answers = [-1 for i in range(n)]

for i in range(n-1, -1, -1):

    while stack and nums[i] >= stack[-1]: # 오름차순으로 쌓여 있는 스택(top이 제일 작음)
        stack.pop()
    
    if stack:
        answers[i] = stack[-1]
    
    stack.append(nums[i])


print(*answers, sep=" ")