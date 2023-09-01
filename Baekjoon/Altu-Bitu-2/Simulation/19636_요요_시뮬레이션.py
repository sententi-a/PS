# 요요 시뮬레이션 https://www.acmicpc.net/problem/19636

"""
|일일 에너지 섭취량 - 일일 에너지 소비량|이 
기초 대사량 변화 역치 T초과시 
해당 값(절대값 아님)의 절반이 일일 기초 대사량에 더해짐
일일 기초 대사량 변화는 같은 날의 체중 변화 다음에 이루어짐

아래의 경우 데시가 사망
- 체중이 0g 이하
- 일일 기초 대사량이 0이하

D일 간의 다이어트가 끝난 후 일일 기초 대사량 변화 고려했을 때 / 안 했을 때 각각의 예상 체중과 일일 기초 대사량을, 다이어트 전 생활로 돌아갈 때 요요가 발생할 지 출력
"""

import sys

before_weight, before_bmr, limit = map(int, sys.stdin.readline().split())
period, after_eat, activity = map(int, sys.stdin.readline().split())

after_weight, after_bmr, yoyo = before_weight, before_bmr, "NO"
first_died, second_died = False, False

for day in range(period):
    consume = after_eat - (after_bmr + activity)
    after_weight += consume

    if abs(consume) > limit:
        after_bmr += consume // 2


if before_bmr - after_bmr > 0:
    yoyo = "YOYO"

not_considered_weight = before_weight + (after_eat - (before_bmr + activity)) * period

if not_considered_weight <= 0:
    print("Danger Diet")
else:
    print(not_considered_weight, before_bmr)

if after_weight <= 0 or after_bmr <= 0:
    print("Danger Diet")
else:
    print(after_weight, after_bmr, yoyo)
