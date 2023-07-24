# 영화감독 숌 https://www.acmicpc.net/problem/1436

"""
종말의 수 : 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수 
666, 1666, 2666, 3666 ... 
N번째 영화 제목 : 세상의 종말 (N번째로 작은 종말의 수)
숌이 만든 N번째 영화의 제목에 들어간 수 출력하기 
"""

import sys

order = int(sys.stdin.readline())

target = 666
cnt = 1

while cnt < order:
    target += 1

    if str(target).find("666") != -1:
        cnt += 1


print(target)
