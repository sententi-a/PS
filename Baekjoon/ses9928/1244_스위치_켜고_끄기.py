# 스위치 켜고 끄기 https://www.acmicpc.net/problem/1244

"""
남 
- 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꿈 (on->off / off->on)

여
- 받은 수와 같은 번호인 스위치를 중심으로 스위치 상태가 좌우로 대칭이면서, 가장 많은 스위치를 포함하는 구간을 찾아
  그 구간에 속한 스위치의 상태를 모두 바꿈 (이 때 상태를 바꿀 스위치 개수는 항상 홀수)

"""

import sys 

switch_cnt = int(sys.stdin.readline())
switches = list(map(int, sys.stdin.readline().split()))
result = [0] + switches[:] # 패딩 추가

student_cnt = int(sys.stdin.readline())
students = []

for _ in range(student_cnt):
    students.append(list(map(int, sys.stdin.readline().split())))

for student in students:
    # 남학생일 때  
    if student[0] == 1:
        for i in range(student[1], switch_cnt+1, student[1]):
            result[i] = not result[i]
    
    # 여학생일 때 
    else:
        target = student[1]
        result[target] = not result[target]
        limit = min(switch_cnt - target, target - 1)
        
        for i in range(1, limit + 1):
            if result[target - i] == result[target + i]:
                result[target - i] = not result[target - i]
                result[target + i] = not result[target + i]
            else:
                break


result = list(map(int, result))

# 한 줄에 20개까지 출력할 수 있음
for i in range(1, switch_cnt + 1):
    print(result[i], end=" ")
    if i % 20 == 0 and i != 0:
        print()