# 집합 https://www.acmicpc.net/problem/11723

"""
add x : S에 x 추가 (이미 있는 경우 연산 무시)
remove x : S에서 x제거 (없는 경우 연산 무시)
check x : S에 x가 있으면 1, 없으면 0 출력
toggle x : S에 x가 있으면 x 제거, 없으면 x 추가
all : S를 {1, 2, 3, 4, ... 20}으로 바꿈
empty : S를 공집합으로 바꿈 
"""

import sys 

operation_cnt = int(sys.stdin.readline())
_set = set()
all_set = set([i for i in range(1, 21)])

for _ in range(operation_cnt):
    _input = sys.stdin.readline().rstrip()

    if _input == 'all' or _input == 'empty':
        if _input == 'all':
            _set = all_set.copy()
        else:
            _set.clear()

    else:
        order, num = _input.split(' ')
        num = int(num)

        if order == 'check':
            if num in _set:
                print(1)
            else:
                print(0)

        elif order == 'add':
            _set.add(num)

        elif order == 'remove':
            _set.discard(num)

        elif order == 'toggle':
            if num in _set:
                _set.remove(num)
            else:
                _set.add(num)


