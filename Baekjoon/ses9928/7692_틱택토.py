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

def hor_continued(case: str, horse: str):
    # print(case)
    for i in range(0, 9, 3):
        cnt = 0

        for j in range(i, i+3):
            if case[j] == horse:
                cnt += 1

        if cnt == 3:
            return True
        
    return False


def vert_continued(case: str, horse: str):
    # 0 3 6 
    # 1 4 7
    # 2 5 8 

    for i in range(3):
        cnt = 0

        for j in range(i, i+7, 3):
            if case[j] == horse:
                cnt += 1

        if cnt == 3:
            return True
        
    return False

def diagonal_continued(case: str, horse: str):
    # 0 4 8 / 2 4 6
    cnt = 0

    for i in range(3):
        if case[i*4] == horse:
            cnt += 1
    
    if cnt == 3:
        return True
    
    cnt = 0

    for i in range(1, 4):
        if case[i*2] == horse:
            cnt += 1

    if cnt == 3:
        return True
    
    return False

def continue_check(case: str, horse: str):
    if hor_continued(case, horse):
        return True
    
    if vert_continued(case, horse):
        return True
    
    if diagonal_continued(case, horse):
        return True
    
    return False

def is_valid(case: str):
    x_cnt = case.count('X')
    o_cnt = case.count('O')
    empty_cnt = case.count('.')

    # X가 O보다 작을 때 (X가 먼저 놓으므로 불가능)
    if x_cnt < o_cnt:
        return 'invalid'
    
    # X가 O보다 큰데 차이가 1이 아닐 경우 (번갈아 놓으므로 차이가 1이 돼야함)
    if x_cnt > o_cnt and x_cnt - o_cnt > 1:
        return 'invalid'

    #----X가 O보다 크거나 같을 때, 클 때는 차이가 1일 때----#
    # X, O 둘 다 이길 수 없음
    if continue_check(case, 'X') and continue_check(case, 'O'):
        return 'invalid'
    # X가 이기면 무조건 X가 O보다 많아야 함
    elif continue_check(case, 'X') and x_cnt > o_cnt:
        return 'valid'
    # O가 이기면 무조건 X와 O가 같아야 함 
    elif continue_check(case, 'O') and x_cnt == o_cnt:
        return 'valid'
    
    # 꽉 찼는데 승패가 갈리지 않았을 때
    if empty_cnt == 0 and not continue_check(case, 'X') and not continue_check(case, 'O'):
        return 'valid'

    return 'invalid'


if __name__ == '__main__':
    answers = []

    while True:
        case = sys.stdin.readline().rstrip()

        # end는 입력의 마지막   
        if case == 'end':
            break

        answers.append(is_valid(case))
    
    print(*answers, sep="\n")