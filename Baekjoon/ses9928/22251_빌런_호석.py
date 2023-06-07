# 빌런 호석 https://www.acmicpc.net/problem/22251

"""
엘리베이터의 층수를 보여주는 디스플레이에는 최대 K 자리의 수가 보임 (수는 0으로 시작할 수도 있음)
LED를 최소 1개 최대 P개 반전시킬 계획
반전 이후에 디스플레이의 수가 1 이상 N 이하(층 범위)가 되도록 바꿀 예정

현재 엘리베이터가 실제로 X층에 멈춰있을 때, 호석이가 반전시킬 LED를 고를 수 있는 경우의 수 계산
"""

import sys

max_floor, digit, max_reverse, curr = map(int, sys.stdin.readline().split())

leds = {
    "0": 0b1110111,
    "1": 0b0010010,
    "2": 0b1011101,
    "3": 0b1011011,
    "4": 0b0111010,
    "5": 0b1101011,
    "6": 0b1101111,
    "7": 0b1010010,
    "8": 0b1111111,
    "9": 0b1111011,
}

# 한 자리 숫자 비교
def get_digit_diff(a, b, digit=7):
    cnt = 0
    diff = bin(leds[a]^leds[b])[2:].zfill(digit)

    for i in range(7):
        if diff[i] == '1':
            cnt += 1

    return cnt

# 여러 자릿수 숫자 비교 
def get_diffs(a, b, digit=digit):
    a = str(a).zfill(digit)
    b = str(b).zfill(digit)

    cnt = 0

    for i in range(digit):
        if a[i] == b[i]:
            continue
        cnt += get_digit_diff(a[i], b[i])

    return cnt

answer = 0

# 1층부터 N층까지 현재 led 상태를 P번 안에 해당 층수로 바꿀 수 있는지 확인 
for i in range(1, max_floor+1):

    if i == curr:
        continue

    if get_diffs(i, curr) <= max_reverse:
        answer += 1


print(answer)