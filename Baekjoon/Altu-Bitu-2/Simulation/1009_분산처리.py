# 분산처리 https://www.acmicpc.net/problem/1009

"""
10대의 컴퓨터가 다음과 같은 방법으로 데이터들을 처리
1 ~ 10번 데이터 : 1 ~ 10번 컴퓨터
11 ~ 20번 데이터 : 1 ~ 10번 컴퓨터

총 데이터의 개수는 항상 a^b개의 형태로 주어질 때, 마지막 데이터가 처리될 컴퓨터 번호는?
"""

import sys

COMPUTERS = 10

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())

    a %= 10

    if a == 0:
        print(10)
        continue

    # 일의 자리의 수 패턴 구하기
    digits = [a]

    temp, cnt = a, 1

    while temp != 1:
        temp = (temp * a) % 10

        if temp == a:
            break

        digits.append(temp)
        cnt += 1

    index = b % cnt - 1

    print(digits[index])
