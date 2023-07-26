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


def calc_score(team, player_cnt, scores):
    score = 0

    # 반복문을 돌면서 n//2C2에 해당하는 조합에 따른 능력치를 쭉 더해줌
    for i in range(player_cnt - 1):
        for j in range(i + 1, player_cnt):
            score += scores[team[i]][team[j]] + scores[team[j]][team[i]]

    return score


for comb in combinations(people, people_cnt // 2):
    team_start = set(comb)
    team_link = set(people) - team_start

    score_start = calc_score(list(team_start), people_cnt // 2, scores)
    score_link = calc_score(list(team_link), people_cnt // 2, scores)

    if abs(score_start - score_link) < min_diff:
        min_diff = abs(score_start - score_link)

print(min_diff)


# zip을 사용해 해당 팀원이 포함된 모든 경우의 능력치 합을 구함
def solution2(people_cnt: int, scores: list):
    member_stat = [sum(i) + sum(j) for i, j in zip(scores, zip(*scores))]
    total_stat = sum(member_stat) // 2

    res = 1e9

    for comb in combinations(member_stat, people_cnt // 2):
        score = abs(total_stat - sum(comb))

        if score < res:
            res = score

    return res
