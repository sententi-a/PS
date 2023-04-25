# 랭킹전 대기열 https://www.acmicpc.net/problem/20006

"""
비슷한 레벨의 플레이어들을 매칭하여 게임을 시작하게 하려고 함

1. 입장 신청시 매칭 가능한 방이 없다면 새로운 방 생성해 입장시킴
    - 이때 해당 방에는 처음 입장한 플레이어의 레벨 기준 -10 ~ +10까지 입장 가능
2. 입장 가능한 방이 있다면 입장시킨 후, 방의 정원이 모두 찰 때까지 대기
    - 입장 가능한 방이 여러 개라면 먼저 생성된 방에 입장
3. 방의 정원이 모두 차면 게임 시작시킴

최종적으로 만들어진 방의 상태와 입장 플레이어들을 출력
"""

import sys 

player_cnt, limit = map(int, sys.stdin.readline().split())
rooms = []

for i in range(player_cnt):
    entered = False

    level, player_id = sys.stdin.readline().split()

    for room in rooms:
        if room[0][0] - 10 <= int(level) <= room[0][0] + 10:
            if len(room) < limit:
                room.append((int(level), player_id))
                entered = True
                break

    if not entered: 
        rooms.append([(int(level), player_id)])


for room in rooms:
    room.sort(key=lambda x: x[1])

    if len(room) == limit:
        print('Started!')
    else:
        print('Waiting!')
    
    for player in room:
        print(*player)