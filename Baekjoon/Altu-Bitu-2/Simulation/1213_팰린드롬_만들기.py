# 팰린드롬 만들기 https://www.acmicpc.net/problem/1213

"""
임한수의 영어 이름의 알파벳 순서를 적절히 바꿔 팰린드롬을 만들려고 함
영어이름은 최대 50글자
불가능할 때는 I'm Sorry Hansoo 출력
정답이 여러개일 경우 사전순으로 출력
"""

import sys
from collections import defaultdict

name = sys.stdin.readline().rstrip()

# 이름이 한자리일 경우
if len(name) == 1:
    print(name)
    exit()

alphabets = defaultdict(int)

# 영어 이름의 각 알파벳이 몇 개인지 dict에 담음
for char in name:
    alphabets[char] += 1

odd_cnt = 0
middle_alphabet = ''

# dict를 돌며 개수가 홀수인 알파벳이 2개 이상이면 팰린드롬 생성불가
for key, value in alphabets.items():
    if value % 2 != 0:
        odd_cnt += 1
        middle_alphabet = key
        alphabets[key] -= 1

    if odd_cnt > 1:
        print("I'm Sorry Hansoo")
        exit()

# dict를 알파벳 사전 순으로 정렬
alphabets = dict(sorted(alphabets.items()))
front = []

# 팰린드롬의 앞부분
for key, value in alphabets.items():
    for i in range(value // 2):
        front.append(key) 

answer = []

# 영어 이름의 길이가 짝수일 때 
if middle_alphabet == '':
    answer = front + front[::-1]
    print(*answer, sep="")
    exit()

# 영어 이름의 길이가 홀수일 때
else:
    answer = front + [middle_alphabet] + front[::-1]
    print(*answer, sep="")
    exit()
