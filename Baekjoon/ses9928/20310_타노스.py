# 타노스 https://www.acmicpc.net/problem/20310

"""
0, 1로 이루어진 문자열 S
S가 포함하는 0의 개수, 1의 개수는 모두 짝수

타노스는 S를 구성하는 문자 중 절반의 0, 절반의 1을 제거해 새로운 문자열 S'를 만들고자 함
S'로 가능한 문자열 중 사전순으로 가장 빠른 것 구하기 (단, 원래 문자열에서 순서가 바뀌면 안 됨)
"""

import sys
from collections import Counter

string = list(sys.stdin.readline().rstrip())

num_counter = Counter(string)

zero_cnt = num_counter['0'] // 2
one_cnt = num_counter['1'] // 2

#-------subtask 1-------#
# answer = ''

# while zero_cnt > 0:
#     answer += '0'
#     zero_cnt -= 1

# while one_cnt > 0:
#     answer += '1'
#     one_cnt -= 1

# print(answer)
#-----------------------#

#-------subtask 2-------#
# 앞에서부터 1을 제거
for i in range(len(string)):
    if string[i] == '1':
        string[i] = ' '
        one_cnt -= 1
    
    if one_cnt <= 0:
        break

# 뒤에서부터 0을 제거
for i in range(len(string)-1, -1, -1):
    if string[i] == '0':
        string[i] = ' '
        zero_cnt -= 1

    if zero_cnt <= 0:
        break 

answer = ''

for num in string:
    if num != ' ':
        answer += num

print(answer)
#-----------------------#
