# Strfry https://www.acmicpc.net/problem/11328

"""
strfry 함수는 입력된 문자열을 무작위로 재배열하여 새로운 문자열을 만들어냄
두 개의 문자열이 주어지면, 2번째 문자열이 1번째 문자열에 strfry 함수를 적용하여 얻어질 수 있는지 판단해야 함
"""
import sys

def answer(str1, str2):
    for char in str1:
        if str1.count(char) == str2.count(char):
            continue
        else:
            return "Impossible"
    return "Possible"

n = int(sys.stdin.readline()) # number of test cases

for _ in range(n):
    case1, case2 = sys.stdin.readline().split()
    print(answer(case1, case2))