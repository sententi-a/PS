# 괄호의 값 https://www.acmicpc.net/problem/2504

"""
() : 2
[] : 3
([]) : 2 * 3 
[()] : 3 * 2
"""

import sys

_input = sys.stdin.readline().rstrip()
answer = 0
temp = 1
stack = [0] # padding added 

for i in range(0, len(_input)):
    # print(_input[i])
    target = _input[i]
    if target == '(':
        temp *= 2
        stack.append('(')
    elif target == '[':
        temp *= 3
        stack.append('[')
    elif target == ')':
        if not stack.pop() == '(':
            print(0)
            exit()
        if _input[i-1] == '(': # 직전 원소가 (일 때만 더하기
            answer += temp
        temp //= 2 
    elif target == ']':
        if not stack.pop() == '[':
            print(0)
            exit()
        if _input[i-1] == '[': # 직전 원소가 [일 때만 더하기
            answer += temp
        temp //= 3
        
    print(f'target: {target}, i: {i}, temp: {temp}, answer: {answer}')

print(answer)


