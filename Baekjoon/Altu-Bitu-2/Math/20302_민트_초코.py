# 민트 초코 https://www.acmicpc.net/problem/20302

"""
정수의 곱셈, 나눗셈으로만 이뤄진 임의의 수식을 적고
그 결과가 정수이면 'mint chocolate', 정수가 아닌 유리수이면 'toothpaste'를 먹는다.
상원이가 적은 수식이 주어졌을 때 어떤 디저트를 먹게 될지 맞혀보기 
"""

import sys

num_cnt = int(sys.stdin.readline())
formula = list(sys.stdin.readline().rstrip().split())

desert = ""

# 정수/유리수를 판별할 수 있는 방법은?
# 수식이 곱셈, 나눗셈으로만 이루어져 있으므로
# 모든 곱셈을 합치고, 모든 나눗셈을 합쳐서 보고 마지막에 이 둘을 나눈 나머지가 0이면 정수

multiply = int(formula[0])
divide = 1

for i in range(1, (num_cnt - 1) * 2, 2):
    operator = formula[i]
    operand = int(formula[i + 1])

    if operator == "*":
        multiply *= operand
    else:
        divide *= operand

if multiply % divide == 0:
    desert = "mint chocolate"
else:
    desert = "toothpaste"

print(desert)
