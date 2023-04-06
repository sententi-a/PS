# ZOAC 4 https://www.acmicpc.net/problem/23971

"""
한 명씩 앉을 수 있는 테이블이 행마다 W개씩 H행에 걸쳐 있을 때,
모든 참가자는 세로로 N칸 / 가로로 M칸 이상 비우고 앉아야 함
-> 모든 참가자와 세로줄 번호의 차가 N보다 크거나 가로줄 번호의 차가 M보다 큰 곳

강의실이 수용할 수 있는 최대 인원 수 출력하기
"""

import sys 
import math

row, col, ver, hor = map(int, sys.stdin.readline().split())

print(math.ceil((row / (ver + 1))) *  math.ceil((col / (hor + 1))))