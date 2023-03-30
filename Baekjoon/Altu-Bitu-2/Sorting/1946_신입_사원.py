# 신입 사원 https://www.acmicpc.net/problem/1946

"""
서류심사, 면접시험 성적이 다른 어떤 지원자보다 모두 떨어진다면 선발 X
이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수 구하기
"""

import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    candidates = []

    count = int(sys.stdin.readline())
    answer = 0

    for i in range(count):
        candidates.append(tuple(map(int, sys.stdin.readline().split())))
    
    candidates.sort(key=lambda x: x[0])
    
    # 앞이랑 비교해야 함 . 앞과 비교했을 때 내가 더 나은 게 없다면 내가 탈락
    # 단순히 앞의 요소 하나만 비교하면 안되고, 
    # 나보다 앞에 있는 원소들 중 합격한 사람 즉, 현재 최고의 면접 순위보다 무조건 내가 더 높아야 함

    criteria = candidates[0]

    for i in range(0, count):
        if candidates[i][1] <= criteria[1]:
            answer += 1
            criteria = candidates[i]
            # print(candidates[i])
    
    print(answer)

