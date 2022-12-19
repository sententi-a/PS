# 회의실 배정 https://www.acmicpc.net/problem/1931

import sys

n = int(sys.stdin.readline()) # 회의 수
schedule = [] # 입력된 회의들 

for _ in range(n):
    schedule.append(tuple(map(int, sys.stdin.readline().split())))

schedule.sort(key= lambda x:(x[1], x[0])) # 종료시간을 기준으로 오름차순 정렬, 종료 시간이 같을 때 시작시간 기준 오름차순 정렬 ((2, 2), (1, 2)의 경우 정답이 2가 나와야 함)

answer = [schedule[0]] # 미팅 순서
prev = 0 # 바로 이전 미팅

for i in range(1, n):
    if schedule[i][0] >= schedule[prev][1]: # 바로 이전 미팅의 종료 시간보다 크되 가장 가까운 시작 시간을 가지는 미팅을 선택함
        answer.append(schedule[i])
        prev = i

print(len(answer))