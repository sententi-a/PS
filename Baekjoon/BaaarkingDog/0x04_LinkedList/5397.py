# 키로거 https://www.acmicpc.net/problem/5397

################### PyPy3 263428KB 2048ms######################
"""
사용자가 키보드를 누른 명령을 모두 기록하는 키로거를 보고 
비밀번호를 알아내는 프로그램 작성하기

알파벳 대문자, 소문자, 숫자, 백스페이스(-), 화살표(<, >)
"""

import sys

for _ in range(int(sys.stdin.readline())):
    case_str = sys.stdin.readline().strip()
  
    cursor = 0
    unused = 1
    
    data = [-1 for _ in range(10**6 + 5)]
    prev = [-1 for _ in range(10**6 + 5)]
    nxt = [-1 for _ in range(10**6 + 5)]

    for i in range(len(case_str)):
        if case_str[i] == '<':
            if prev[cursor] != -1:
                cursor = prev[cursor]
    
        elif case_str[i] == '>':
            if nxt[cursor] != -1:
                cursor = nxt[cursor]
    
        elif case_str[i] == '-':
            if cursor <= 0 or prev[cursor] == -1:
                continue
            
            if nxt[cursor] != -1:
                prev[nxt[cursor]] = prev[cursor]
            nxt[prev[cursor]] = nxt[cursor]

            cursor = prev[cursor]

        else:
            data[unused] = case_str[i]
            prev[unused] = cursor
            nxt[unused] = nxt[cursor]

            if nxt[cursor] != -1:
                prev[nxt[cursor]] = unused
            nxt[cursor] = unused

            cursor = nxt[cursor]
            unused += 1
    
    
    current = nxt[0]

    while current != -1:
        print(data[current], end="")
        current = nxt[current]
    print()