# 국영수 https://www.acmicpc.net/problem/10825
"""
학생 성적에 따라 정렬
1. 국어 점수 내림차순
2. 영어 점수 오름차순
3. 수학 점수 내림차순
4. 이름 사전 오름차순
"""

import sys

n = int(sys.stdin.readline())
students = []

for i in range(n):
    students.append(list(sys.stdin.readline().rstrip().split(" ")))

students.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(len(students)):
    print(students[i][0])
    