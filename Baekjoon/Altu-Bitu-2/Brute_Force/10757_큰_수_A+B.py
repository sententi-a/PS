# 큰 수 A+B https://www.acmicpc.net/problem/10757

"""
두 정수 A, B를 입력받은 후, A+B를 출력하기
"""

import sys

a, b = sys.stdin.readline().rstrip().split()


def solution1(a, b):
    a_digits = len(a)
    b_digits = len(b)

    if a_digits > b_digits:
        b = "0" * (a_digits - b_digits) + b

    else:
        a = "0" * (b_digits - a_digits) + a

    answer = 0

    for square in range(max(a_digits, b_digits)):
        index = max(a_digits, b_digits) - 1 - square
        answer += (10**square) * (int(a[index]) + int(b[index]))

    return answer


def solution2(a, b):
    a_digits = len(a)
    b_digits = len(b)

    length = max(a_digits, b_digits)

    if a_digits > b_digits:
        b = "0" * (length - b_digits) + b

    else:
        a = "0" * (length - a_digits) + a

    # 정답 배열 (각 인덱스의 값은 각 자리수의 값이 됨)
    answer = [0 for _ in range(length + 1)]

    for i in range(length, 0, -1):
        answer[i] += int(a[i - 1]) + int(b[i - 1])
        answer[i - 1] = answer[i] // 10
        answer[i] %= 10

    return int("".join(map(str, answer)))


print(solution2(a, b))
