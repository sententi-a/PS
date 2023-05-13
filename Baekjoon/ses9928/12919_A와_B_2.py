# A와 B 2 https://www.acmicpc.net/problem/12919

"""
- 문자열의 뒤에 A를 추가한다
- 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다
문자열 S를 T로 바꿀 수 있으면 1, 없으면 0 출력
"""

import sys
from collections import Counter

start = sys.stdin.readline().rstrip()
goal = sys.stdin.readline().rstrip()

examine = list(goal)

start_counter = Counter(start)
goal_counter = Counter(goal)

if goal_counter['A'] < start_counter['A'] or goal_counter['B'] < start_counter['B']:
    print(0)
    exit()

add_counter = goal_counter - start_counter

while len(start) != len(examine):
    # A를 먼저 제거해야 하는 경우 / B를 제거해야 하는 경우 조건 생각하기 
    if add_counter['A'] and examine[-1] == 'A':
        examine.pop()
        add_counter['A'] -= 1

    # B가 추가되었다면 무조건 그 B는 맨 앞으로 갔음
    elif add_counter['B'] and examine[0] == 'B':
        examine = examine[1:]
        examine = examine[::-1]
        add_counter['B'] -= 1

    else:
        print(0)
        exit()

if start == "".join(examine):
    print(1)

else:
    print(0)

# BAAAAABAA 
# BAAAAABAA'B'
# 'B'AABAAAAAB

# A
# A'B'
# 'B'A
# BA'B'
# 'B'AB
# BABA

# A
# A'B'
# 'B'A
# BA'B'
# 'B'AB

# BA
# BAA
# BAAB
# BBAAB