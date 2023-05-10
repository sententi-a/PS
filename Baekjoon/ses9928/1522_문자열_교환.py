# 문자열 교환 https://www.acmicpc.net/problem/1522

"""
a, b로만 이루어진 문자열이 주어질 때,
a를 모두 연속으로 만들기 위해 필요한 최소 교환 횟수 구하기
문자열은 원형이므로, 처음과 끝은 서로 인접해있음 
"""

import sys

string = sys.stdin.readline().rstrip()

a_cnt = string.count('a')


if a_cnt == len(string) or a_cnt == 0:
    print(0)
    exit()

# a의 개수만큼 a가 연속적이면 되므로 a의 개수만큼 영역을 만들고, 그 안의 영역은 모두 a로 만들겠다고 생각하면 됨
# 그래서 a의 개수가 4라면 길이가 4로 된 영역을 만들고, 그 안에 있는 b를 모두 외부의 a와 교환하면 됨

# 초기값
b_cnt = answer = string[:a_cnt].count('b')

for i in range(len(string)-1):
    start, end = i, (i + a_cnt) % len(string)
    print(start, end, b_cnt)

    if string[start] == 'b':
        b_cnt -= 1
    
    if string[end] == 'b':
        b_cnt += 1

    if answer > b_cnt:
        answer = b_cnt

print(answer)