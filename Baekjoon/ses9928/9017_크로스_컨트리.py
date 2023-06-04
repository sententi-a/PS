# 크로스 컨트리 https://www.acmicpc.net/problem/9017

"""
한 팀은 6명의 선수로 구성, 팀 점수는 상위 네 명의 점수를 합해 계산
점수는 자격을 갖춘 팀의 주자들에게만 주어지고, 결승점을 통과한 순서대로 점수 받음
이 점수를 더해 가장 낮은 점수를 얻는 팀이 우승
- 6명의 주자가 참가하지 못한 팀은 점수 계산에서 제외
- 동점의 경우 다섯 번째 주자가 가장 빨리 들어온 팀이 우승 

* 여섯 명보다 많은 선수가 참가하는 팀은 없음 
* 적어도 한 팀은 참가 선수가 여섯이고, 모든 선수는 끝까지 완주
"""

import sys 
from collections import Counter
from collections import defaultdict

answers = [] 

for _ in range(int(sys.stdin.readline())):
    player_cnt = int(sys.stdin.readline())
    _input = list(map(int, sys.stdin.readline().split()))

    # 팀의 참가 선수가 6명보다 적으면 점수 계산에서 제외
    counter = Counter(_input)

    for key, val in list(counter.items()):
        if val < 6:
            del counter[key]

    # 각 팀마다 선수가 몇 번째로 들어왔는지 계산 (제외된 팀의 팀원은 계산하지 않음)
    rank = 1
    teams = set(counter.keys())
    players = defaultdict(list)

    for i in range(player_cnt):
        if _input[i] in teams:
            players[_input[i]].append(rank)
            rank += 1

    # 상위 4명의 점수 계산해 어느 팀이 이겼는지 계산
    answer, score = 0, 10**9

    for team, arr in players.items():
        score_of_four = sum(arr[:4])

        if score_of_four < score:
            answer = team
            score = score_of_four
        
        elif score_of_four == score:
            if arr[4] < players[answer][4]: 
                answer = team
                score = score_of_four

        # print(_, team, arr, answer, score)

    answers.append(answer)


print(*answers, sep="\n")  