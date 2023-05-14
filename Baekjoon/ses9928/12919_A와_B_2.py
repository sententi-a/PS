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

# 1st 시도 : 반복문을 통해 A/B 하나씩 제거하면서 되돌아감 
# examine = goal

# start_counter = Counter(start)
# goal_counter = Counter(goal)

# if goal_counter['A'] < start_counter['A'] or goal_counter['B'] < start_counter['B']:
#     print(0)
#     exit()

# add_counter = goal_counter - start_counter

# while True:
#     # print(examine)

#     if len(examine) < len(start):
#         print(0)
#         exit() 

#     if start == examine:
#         print(1)
#         exit() 

#     if add_counter['A'] and examine[-1] == 'A':
#     # if examine[-1] == 'A':
#         examine = examine[:-1]
#         add_counter['A'] -= 1

#     # B가 추가되었다면 무조건 그 B는 맨 앞으로 갔음
#     elif examine[0] == 'B':
#         examine = examine[1:][::-1]

#     else:
#         print(0)
#         exit()

# 2nd 시도 : backtracking 원리를 차용한 반복문 사용 
stack = [goal]
flag = False 

while stack:
    arr = stack.pop()

    if len(arr) == len(start):
        if arr == start:
            flag = True
            break
        continue

    if arr[-1] == 'A':
        new_arr = arr[:-1]
        stack.append(new_arr)

    if arr[0] == 'B':
        new_arr = arr[1:][::-1]
        stack.append(new_arr)

print(1 if flag else 0)

# B를 없애야 할 때랑, A를 없애야 할 때가 있는데 둘의 조건에 모두 해당하는 경우의 수가 있음 
# BAA 같은 것들.. 이럴 때는 backtracking하면 되나?
# 그런데 재귀를 쓰기는 싫음

# backtracking을 했어야 했어.. 근데 backtracking 없는 재귀로 되는 이유는 무엇일까? 
# backtracking을 반복문으로 바꾸려면? stack + copy를 사용해 원본에 손상이 가지 않게 