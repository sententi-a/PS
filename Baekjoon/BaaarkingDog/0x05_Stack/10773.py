# 제로 https://www.acmicpc.net/problem/10773

####################	31232KB	80ms  #######################
"""
입력한 정수가 0일 경우 가장 최근에 쓴 수를 지우고, 
아닐 경우 해당 수를 씀. 최종적으로는 남아있는 수의 합을 출력.
"""

import sys

stack = []

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))