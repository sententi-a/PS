# 0 만들기 https://www.acmicpc.net/problem/7490

"""
1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N
그리고 + / - / (공백)을 숫자 사이에 삽입해 그 결과가 0이 될 수 있는지 살펴보기
N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램 작성 
"""

import sys 
sys.setrecursionlimit(10**9)

def get_sum_from_formula(formula, total):
    answer = ""

    for i in range(len(formula)- 1, -1, -1):
        if formula[i] == '+':
            return total - int(formula[i+1]) + int(answer)
            
        elif formula[i] == '-':
            return total + int(formula[i+1]) - int(answer)
            
        elif formula[i] == " ":
            continue

        answer = formula[i] + answer
    
    return int(answer)

def calc(curr, limit, total, formula, add, sub):
    if add:
        formula = formula + "+" + str(curr)
        total += curr

    elif sub:
        formula = formula + "-" + str(curr)
        total -= curr

    else:
        if curr == 1:
            formula = str(curr)
        else:
            formula = formula + " " + str(curr)
            total = get_sum_from_formula(formula, total)


    if curr == limit:
        if total == 0:
            answer.append(formula)
            return
        return
    
    # 더하기
    calc(curr + 1, limit, total, formula, True, False)
    # 빼기
    calc(curr + 1, limit, total, formula, False, True)
    # 붙이기
    calc(curr + 1 ,limit, total, formula, False, False)


tc_cnt = int(sys.stdin.readline())

answers = []

for _ in range(tc_cnt):
    n = int(sys.stdin.readline())

    answer = []
    calc(1, n, 1, "", False, False)
    answer.sort()
    answers.append(answer)


for i in range(tc_cnt):
    for formula in answers[i]:
        print(formula)

    if i < tc_cnt - 1:
        print()
