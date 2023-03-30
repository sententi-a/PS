# 싸이버개강총회 https://www.acmicpc.net/problem/19583

"""
개강총회를 유튜브 스트리밍으로 대체하면 생기는 문제
1. 누가 개강총회에 왔는지 알 수 없음
2. 누가 개강총회 자리에 끝까지 남아있었는지 알 수 없음
3. 어떤 사람이 개강총회 스트리밍을 단순히 틀어놓기만 했는지 알 수 없음

해결책
1. 개강총회 시작 전 : 입장 확인 여부 확인 (개강총회 시작 시간 이전에 대화한 적 있는 학회원의 닉네임 체크)
2. 개강총회 종료 후 : 스트리밍을 끝낼 때까지 퇴장 여부 확인 (개강총회 끝나고 스트리밍이 끝날 때까지 대화한 적이 있는 학회원의 닉네임 체크)

입장부터 퇴장까지 모두 확인된 학회원은 몇 명?
"""

import sys

start, finish, end = sys.stdin.readline().split()
start = list(map(int, start.split(':'))) 
start = start[0] * 3600 + start[1] * 60

finish = list(map(int, finish.split(':')))
finish = finish[0] * 3600 + finish[1] * 60

end = list(map(int, end.split(":")))
end = end[0] * 3600 + end[1] * 60

check_in = set()
answer = 0

while True:
    try:
        time, nickname = sys.stdin.readline().split()
        time = list(map(int, time.split(":")))
        time = time[0] * 3600 + time[1] * 60
    except:
        break
    
    # 시작 전 명단 체크
    # if time[0] < start[0] or (time[0] == start[0] and time[1] <= start[1]):
        # check_in.add(nickname)
    if time <= start:
        check_in.add(nickname)

    # 종료 후 명단 체크    
    # elif (time[0] > finish[0] or (time[0] == finish[0] and time[1] >= finish[1])) and time[0] < end[0] or 
    elif finish <= time <= end:
        if nickname in check_in:
            answer += 1
            check_in.remove(nickname)

print(answer)