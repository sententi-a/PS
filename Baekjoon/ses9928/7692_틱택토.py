# 틱택토 https://www.acmicpc.net/problem/7682

"""
3*3 게임판에 두 사람이 각각 X / O 말을 번갈아가면서 놓음
반드시 첫 번째 사람이 X를 놓고, 두 번째 사람이 O를 놓음

[게임이 끝나는 경우]
- 한 사람의 말이 가로, 세로, 대각선 방향으로 3칸을 잇는 데 성공
- 게임판이 가득 참 

게임판의 상태가 주어졌을 때, 그 상태가 발생할 수 있는 최종 상태인지 판별
(입력은 여러 개의 테케로 이루어져 있고, 각 줄은 9개의 문자 포함. .은 빈칸)
"""

import sys 

def hor_continued(case: str):
    print(case)
    for i in range(0, 9, 3):
        flag = True

        for j in range(i+1, i+3):
            if case[j-1] != case[j]:
                flag = False
                break
        
        if flag:
            return flag
        
    return flag


def vert_continued(case: str):
    # 0 3 6 
    # 1 4 7
    # 2 5 8 

    for i in range(3):
        flag = True

        for j in range(i+3, i+7, 3):
            if case[j-3] != case[j]:
                flag = False
                break

        if flag:
            return flag
        
    return flag

def diagonal_continued(case):
    flag = True

    for i in range(1, 3):
        if case[(i-1) * 4] != case[i*4]:
            flag = False
            break

    if flag:
        return flag
    
    flag = True

    for i in range(2, 4):
        if case[(i-1) * 2] != case[i * 2]:
            flag = False
            break

    return flag


def is_valid(case: str):
    x_cnt = case.count('X')
    o_cnt = case.count('O')

    # X가 O보다 작거나 같을 때 (X가 먼저 놓으므로 불가능)
    if x_cnt <= o_cnt:
        return 'invalid'
    
    # X가 O보다 큰데 차이가 1이 아닐 경우 (번갈아 놓으므로 차이가 1이 돼야함)
    elif x_cnt - o_cnt != 1:
        return 'invalid'

    # 가로 3칸 
    if hor_continued(case):
        return 'valid'
    
    # 세로 3칸
    if vert_continued(case):
        return 'valid'

    # 대각선 3칸
    # abs(x1-x2) == abs(y1-y2)
    # 00 11 22 / 02 11 20
    # 0 4 8 / 2 4 6
    if diagonal_continued(case):
        return 'valid'


    return 'invalid'
    
answers = []

while True:
    case = sys.stdin.readline().rstrip()

    # end는 입력의 마지막   
    if case == 'end':
        break

    answers.append(is_valid(case))


print(*answers, sep="\n")

# .XX
# X.X
# OOO