# 민트 초코 https://www.acmicpc.net/problem/20302

"""
정수의 곱셈, 나눗셈으로만 이뤄진 임의의 수식을 적고
그 결과가 정수이면 'mint chocolate', 정수가 아닌 유리수이면 'toothpaste'를 먹는다.
상원이가 적은 수식이 주어졌을 때 어떤 디저트를 먹게 될지 맞혀보기 
"""

import sys

MAXNUM = 100000


def get_min_prime_num(n: int = MAXNUM):
    """
    인덱스에 해당하는 숫자의 최소 약수 (소수)를 저장하는 배열을 리턴하는 함수
    """
    min_prime_num = [i for i in range(n + 1)]

    for i in range(2, int(n**0.5) + 1):
        if min_prime_num[i] == i:
            for j in range(i * 2, n + 1, i):
                if min_prime_num[j] == j:
                    min_prime_num[j] = i

    return min_prime_num


def calculate(formula: list, min_prime_num: list):
    """
    수식과 숫자의 최소 약수를 담은 배열을 파라미터로 받아,
    수식의 결과가 유리수인지 정수인지 판별하는 함수
    """
    answer = [0 for _ in range(MAXNUM + 1)]
    min_prime_num = get_min_prime_num()

    for i in range(1, len(formula), 2):
        operator = formula[i - 1]
        operand = abs(int(formula[i]))

        # 0을 곱하면 0이므로 정수
        if operand == 0:
            return "mint chocolate"

        # 곱셈이면 약수의 거듭제곱 수를 + 1, 나눗셈이면 -1
        if operator == "*":
            flag = 1
        else:
            flag = -1

        # 각 숫자 소인수분해하기
        while operand > 1:
            answer[min_prime_num[operand]] += flag
            operand //= min_prime_num[operand]

    for cnt in answer[2:]:
        # 나누어 떨어지지 않으면
        if cnt < 0:
            return "toothpaste"

    return "mint chocolate"


if __name__ == "__main__":
    num_cnt = int(sys.stdin.readline())
    formula = ["*"] + list(sys.stdin.readline().rstrip().split())

    desert = calculate(formula, get_min_prime_num())

    print(desert)
