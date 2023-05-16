# 문자열 게임 2 https://www.acmicpc.net/problem/20437

"""
- 알파벳 소문자로 이루어진 문자열 W
- 양의 정수 K
- 어떤 문자를 정확히 K개 포함하는 가장 짧은 연속 문자열의 길이 구함
- 어떤 문자를 정확히 K개 포함하고, 문자열의 첫 번째, 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이 구하기
위와 같은 방식으로 게임을 T회 진행
"""

import sys

for _ in range(int(sys.stdin.readline())):
    string = sys.stdin.readline().rstrip()
    limit = int(sys.stdin.readline())

    start, end = 0, 0

    scs = 0 # 가장 짧은 연속 문자열
    lcs = 0 # 가장 긴 연속 문자열 


    while start <= end and end < len(string)-1:
        # 투포인터 사용
        pass
