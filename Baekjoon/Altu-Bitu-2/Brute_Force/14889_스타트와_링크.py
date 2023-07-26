# 스타트와 링크 https://www.acmicpc.net/problem/14889

"""
축구를 하기 위해 모인 사람은 총 N명 (짝수)
스타트팀 & 링크팀 : 각각 N/2명
Sij = i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치 (Sij != Sji)
팀의 능력치 = 팀에 속한 모든 쌍의 능력치 Sij의 합 
스타트 팀과 링크 팀의 능력치 차이를 최소로 하려고 할 때, 이 최솟값을 출력하기
"""

import sys
from itertools import combinations

people_cnt = int(sys.stdin.readline())
people = [i for i in range(people_cnt)]
scores = []

for _ in range(people_cnt):
    scores.append(list(map(int, sys.stdin.readline().split())))

min_diff = 100 * 400

for comb in combinations(people, people_cnt // 2):
    team_start = set(comb)
    team_link = set(people) - team_start

    # index 사용을 위해 set -> list로 변경
    team_start = list(team_start)
    team_link = list(team_link)

    score_start = 0
    score_link = 0

    # 반복문을 돌면서 n//2C2에 해당하는 조합에 따른 능력치를 쭉 더해줌
    for i in range(people_cnt // 2 - 1):
        for j in range(i + 1, people_cnt // 2):
            score_start += (
                scores[team_start[i]][team_start[j]]
                + scores[team_start[j]][team_start[i]]
            )
            score_link += (
                scores[team_link[i]][team_link[j]] + scores[team_link[j]][team_link[i]]
            )

    if abs(score_start - score_link) < min_diff:
        min_diff = abs(score_start - score_link)

print(min_diff)
