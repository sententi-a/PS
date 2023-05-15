# 컨베이어 벨트 위의 로봇 https://www.acmicpc.net/problem/20055

"""
길이 N인 컨베이어 벨트, 길이 2N인 벨트
벨트는 2N개의 칸으로 나뉘어져 있고, 번호가 매겨짐
[초기 위치]
1, 2, ... N 
2N, 2N-1, ... N+1

1번 위치 : 올리는 위치, N번 위치 : 내리는 위치
로봇은 올리는 위치에만 올릴 수 있고, 내리는 위치에 도달 즉시 내림
로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 1만큼 감소

로봇들을 건너편으로 옮기는 게 미션!
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동함
   즉, 이동하려는 칸에 로봇이 없고, 그 칸의 내구도가 1이상
3. 올리는 위치에 있는 칸의 내구도가 1 이상이면 올리는 위치에 로봇 올림
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료, 그렇지 않다면 1번으로 돌아감 

종료되었을 때 몇 번째 단계가 진행 중이었는지 구하기
"""

import sys 

length, zero_cnt = map(int, sys.stdin.readline().split())
durability = list(map(int, sys.stdin.readline().split()))

is_robot = [False for _ in range(2*length)]

prev = [i-1 for i in range(2*length)]
prev[0] = 2*length-1
nxt = [i for i in range(1, 2*length+1)]
nxt[2*length-1] = 0

# 내구성이 0인 칸의 개수
used = 0

def load_robot(point):
    global used 

    is_robot[point] = True
    durability[point] -= 1

    if durability[point] == 0:
        used += 1

process = 0
on_point = 0

while used < zero_cnt:
    process += 1

    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다
    on_point = prev[on_point]
    off_point = (on_point + length - 1) % (2 * length)

    # 2. 로봇 이동
    # 먼저, 내리는 위치 로봇이 있다면 먼저 내려줌
    point = off_point

    if is_robot[point]:
        is_robot[point] = False

    # 컨베이어 벨트 위 모든 로봇 확인
    for i in range(length-1):
        point = prev[point]

        if is_robot[point]:
            if not is_robot[nxt[point]] and durability[nxt[point]] > 0:
                is_robot[point] = False
                load_robot(nxt[point])
                
                # 로봇을 옮긴 곳이 내리는 위치라면, 바로 다시 내려줌
                if nxt[point] == off_point:
                    is_robot[off_point] = False

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇 올림
    if durability[on_point] > 0:
        load_robot(on_point)

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
    if used >= zero_cnt:
        break


print(process)