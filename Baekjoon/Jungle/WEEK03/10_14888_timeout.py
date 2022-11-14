# 연산자 끼워넣기 acmicpc.net/problem/14888
# python으로는 시간초과 pypy로는 통과

import sys
from itertools import permutations

n = int(sys.stdin.readline()) # 수의 개수
nums = list(map(int, sys.stdin.readline().split())) # 숫자

op_num = list(map(int, sys.stdin.readline().split())) # 각 연산자의 개수 

ops = ['+'] * op_num[0] + ['-'] * op_num[1] + ['*'] * op_num[2] + ['//'] * op_num[3] # 연산자 리스트 

max_res = - (10 ** 9) # 결과의 최댓값
min_res = 10 ** 9 # 결과의 최솟값

for op in permutations(ops): # prefix 느낌으로 계산
    op = list(op)
    num_list = []
    for i in range(len(nums)-1, -1, -1):
        num_list.append(nums[i])

    while len(op) > 0:
        operator = op.pop()
        # print(op, num_list)
        a = num_list.pop()
        b = num_list.pop()
        if operator == '+':
            num_list.append(a+b)
        elif operator == '-':
            num_list.append(a-b)
        elif operator == '*':
            num_list.append(a*b)
        else:
            if a < 0 :
                num_list.append(-(-a//b))
            else:
                num_list.append(a//b)
        
    answer = num_list.pop() # 각 케이스마다의 결과값 
    max_res = max(max_res, answer)
    min_res = min(min_res, answer)

print(max_res)
print(min_res)