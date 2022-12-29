# 신입사원 https://www.acmicpc.net/problem/1946

import sys 

T = int(sys.stdin.readline()) # 테스트 케이스 개수 

for _ in range(T):
    n = int(sys.stdin.readline()) # 지원자의 수 
    grades = []
    for i in range(n):
        grades.append(tuple(map(int, sys.stdin.readline().split())))

    grades.sort(key=lambda x:x[0])

    accepted = grades[0] # 비교 초기 값
    answer = []

    for i in range(n):
        if grades[i][1] <= accepted[1]: # 합격자
            answer.append(grades[i])
            accepted = grades[i]
            
    print(len(answer))
    # print(*answer)


# 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원 수




