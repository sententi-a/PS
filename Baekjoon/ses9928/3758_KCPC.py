# KCPC https://www.acmicpc.net/problem/3758

"""
총 k개의 문제를 풂 
어떤 문제에 대해 풀이를 서버에 제출하면 0-100점 사이 점수를 얻음
- 풀이 제출한 팀의 ID, 문제 번호, 점수 (점수가 제출되는 시간 순대로 저장)
- 한 문제에 대한 풀이를 여러 번 제출할 수 있고, 그 중 최고 점수가 그 문제에 대한 최종 점수가 됨

[팀의 최종 점수] 각 문제에 대해 받은 점수의 총합
[순위] 팀보다 높은 점수를 받은 팀의 수 + 1
- 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높음
- 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높음

우리 팀의 순위를 출력하기 
"""

import sys 

answer = []

tc_cnt = int(sys.stdin.readline())

for _ in range(tc_cnt):
    team_cnt, prob_cnt, my_team, log_cnt = map(int, sys.stdin.readline().split())

    info = [[i+1, [0 for _ in range(prob_cnt)]] for i in range(team_cnt)]
    submit_cnt = [0 for _ in range(team_cnt)]
    last_submit_time = [0 for _ in range(team_cnt)]

    for i in range(log_cnt):
        team_num, prob_num, score = map(int, sys.stdin.readline().split())
        
        submit_cnt[team_num - 1] += 1
        last_submit_time[team_num - 1] = i

        if info[team_num - 1][1][prob_num - 1] < score:
            info[team_num - 1][1][prob_num - 1] = score
    
    info.sort(key=lambda x: (-sum(x[1]), submit_cnt[x[0] - 1], last_submit_time[x[0] - 1]))

    for i in range(team_cnt):
        if info[i][0] == my_team:
            answer.append(i+1)
            break

print(*answer, sep="\n")