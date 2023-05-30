# 숫자고르기 https://www.acmicpc.net/problem/2668

"""
세로 2줄, 가로 N개의 칸으로 이루어진 표가 있음 
- 첫째 줄의 각 칸에는 정수 1, 2, ..., N이 차례로 들어 있음
- 둘째 줄의 각 칸에는 1이상 N이하인 정수가 무작위로 들어 있음

첫째 줄에서 숫자를 적절히 뽑았을 때, 
첫째 줄에서의 숫자 집합과 둘째 줄에서의 숫자 집합이 일치해야 함(1, 3, 5 / 3, 1, 5)
뽑힌 정수들의 개수가 최대가 되도록 하기! 
"""

import sys 

n = int(sys.stdin.readline())

answers = set()

table = [0 for _ in range(n+1)]

# 테이블 채우기
for i in range(n):
    table[i+1] = int(sys.stdin.readline())

    if i+1 == table[i+1]:
        answers.add(i+1)


def count_set(table: list, idx: int):
    elem = table[idx]

    indexes = set([idx])
    elems = set([elem])

    while True:

        idx = elem
        elem = table[idx]

        # 1-3, 3-1과 같은 경우
        if idx in indexes and elem in elems:
            break

        indexes.add(idx)
        elems.add(elem)

    # 두 줄의 집합이 같다면 answer에 추가
    if len(indexes - elems) == 0:
        answers.update(indexes)


# 1부터 N까지 조건에 맞는 경우의 수가 있는지 확인 
for i in range(1, n+1):
    count_set(table, i)


print(len(answers))
print(*sorted(list(answers)), sep="\n")