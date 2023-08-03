# Four Squares https://www.acmicpc.net/problem/17626

"""
모든 자연수는 넷 혹은 그 이하의 제곱수의 합(2제곱/4제곱)으로 표현할 수 있다. 
26 = 5^2 + 1^2 or 4^2 + 3^2 + 1^2
자연수 n이 주어질 때 n을 최소 개수의 제곱수 합으로 표현할 때 그 제곱수들의 최소 개수 출력
"""

import sys

number = int(sys.stdin.readline())
table = [i for i in range(number + 1)]


def get_min_cnt(table: list, number: int):
    answer = table[number]

    for i in range(1, int(number**0.5) + 1):
        if table[number - i**2] < answer:
            answer = table[number - i**2]

    return answer + 1  # 제곱수 하나를 더해줘야 한다.


for num in range(2, number + 1):
    table[num] = get_min_cnt(table, num)

print(table[number])
