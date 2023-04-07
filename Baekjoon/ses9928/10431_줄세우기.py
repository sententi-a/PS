# 줄세우기 https://www.acmicpc.net/problem/10431

"""
강산이네 반 아이들은 항상 20명이고, 중복 키 없음 (오름차순)
한 명을 뽑아 맨 앞에 세우고, 다음 학생이 줄을 설 땐 다음 과정을 거침
- 자기 앞에 자기보다 키가 큰 학생이 없으면 그 자리에 섬
- 있으면 가장 앞에 서고, A부터 뒤까지 한 발씩 물러섬

모든 학생들이 뒤로 물러난 걸음 수의 총합 출력
"""

import sys 

tc_cnt = int(sys.stdin.readline())

for _ in range(tc_cnt):
    _input = list(map(int, sys.stdin.readline().split()))
    tc_num, students = _input[0], _input[1:]

    back_cnt = 0

    for i in range(20): # target 
        for j in range(0, i): # 비교할 앞 배열
            if students[i] < students[j]:
                students[i], students[j] = students[j], students[i]
                back_cnt += 1

    print(tc_num, back_cnt)