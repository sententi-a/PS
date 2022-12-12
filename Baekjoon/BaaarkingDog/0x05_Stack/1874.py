# 스택 수열 https://acmicpc.net/problem/1874

####################36784KB	168ms####################
"""
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 계산하는 프로그램을 작성하라
"""

import sys

n = int(sys.stdin.readline())

prev = 0

stack = []
answer = []

for i in range(n):
    curr = int(sys.stdin.readline())

    # 이전에 pop했던 숫자보다 지금 보는 숫자가 크거나 같다면
    if curr >= prev:
        for j in range(prev+1, curr+1):
            stack.append(j)
            answer.append('+')
        # stack에서 pop한 원소가 지금 보낸 숫자와 같다면 - 붙여주고, prev 변수 갱신 
        if curr == stack.pop():
            answer.append('-')
            prev = curr
        
        else:
            print("NO")
            exit(0)
    
    # 이전에 pop했던 숫자보다 지금 보는 숫자가 작다면
    else:
        # stack에서 pop한 원소와 같아야 제대로된 스택 수열임
        if stack.pop() == curr:
            answer.append('-')
        else:
            print("NO")
            exit(0)

print(*answer, sep="\n")