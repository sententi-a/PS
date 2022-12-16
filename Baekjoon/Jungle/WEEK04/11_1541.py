# 잃어버린 괄호 https://acmicpc.net/problem/1541
import re 
import sys 

_input = sys.stdin.readline().strip()
case = re.split('([+|-])', _input)

div = len(case)

for i in range(1, len(case)):
    if case[i] == '-': # -가 들어있는 인덱스 찾음
        div = i
        break

min_sum = 0

for i in range(0, div, 2):
    min_sum += int(case[i]) # -를 만나기 전까지는 모두 더함

for i in range(div+1, len(case), 2):
    min_sum -= int(case[i]) # -를 만난 후에는 모두 뺌 

print(min_sum)