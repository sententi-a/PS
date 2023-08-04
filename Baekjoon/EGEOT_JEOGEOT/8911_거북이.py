# 거북이 https://www.acmicpc.net/problem/8911

"""
F : 한 눈금 앞으로 
B : 한 눈금 뒤로
L : 왼쪽 90도 회전
R : 오른쪽 90도 회전 

L, R 명령일 때 로봇은 이동하지 않고 방향만 바꿈
거북이는 가장 처음에 (0, 0)에 있고, 북쪽을 쳐다보고 있음
거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이 구하기 (선분의 경우 넓이는 0)
"""

import sys


def update_points(x: int, y: int, points: list):
    # left, right, up, down
    if x < points[0]:
        points[0] = x

    elif x > points[1]:
        points[1] = x

    elif y > points[2]:
        points[2] = y

    elif y < points[3]:
        points[3] = y


def go(commands: str):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    x, y, direction = 0, 0, 0
    points = [0, 0, 0, 0]  # left, right, up, down

    for command in commands:
        if command == "F":
            x += dirs[direction][0]
            y += dirs[direction][1]

        elif command == "B":
            x += -dirs[direction][0]
            y += -dirs[direction][1]

        elif command == "L":
            direction -= 1

            if direction < 0:
                direction = 3

        else:
            direction = (direction + 1) % 4

        update_points(x, y, points)

    return (points[1] - points[0]) * (points[2] - points[3])


if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline())):
        commands = sys.stdin.readline().rstrip()
        answer = go(commands)
        print(answer)
