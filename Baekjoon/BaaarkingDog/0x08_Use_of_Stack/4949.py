# 균형잡힌 세상 4949

"""
어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하기
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류

문자열이 균형을 이루는 조건
- 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
- 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
- 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
- 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
- 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
"""

import sys

while(1):
    string = sys.stdin.readline().rstrip()
    
    if string == '.':
        break

    stack = []
    answer = "yes"
    
    for char in string:
        if char == '[':
            stack.append(char)

        elif char == '(':
            stack.append(char)
        
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                answer = "no"
                break
        
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                answer = "no"
                break
    
    if stack:
        answer = "no"
    
    print(answer)