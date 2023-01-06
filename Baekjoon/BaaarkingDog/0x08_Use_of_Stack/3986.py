# 좋은 단어 https://www.acmicpc.net/problem/3986

"""
같은 글자(A or B)끼리 쌍을 짓기로 하고,
선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝지을 수 있다면 좋은 단어
"""
import sys

count = 0 

for _ in range(int(sys.stdin.readline().rstrip())):
    stack = []
    string = sys.stdin.readline().rstrip()

    # string의 길이가 홀수라면 짝이 맞지 않는 것
    if len(string) % 2 != 0:
        continue
    
    
