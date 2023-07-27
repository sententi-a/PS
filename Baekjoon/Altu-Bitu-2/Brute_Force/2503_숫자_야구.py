# 숫자 야구 https://www.acmicpc.net/problem/2503

"""
영수 : 1-9의 서로 다른 숫자 3개로 구성된 세 자리 수를 생각
민혁 : 그 세 자리 수를 영수에게 물음
=> 스트라이크 : 동일한 자리, 동일한 수 
=> 볼 : 세 자리 수에 있긴 하지만, 다른 자리 

민혁, 영수의 질답이 입력으로 주어질 때,
가능한 답의 총 개수를 출력하기
"""

import sys
from itertools import permutations

answers = set()


def get_all_combinations():
    """
    서로 다른 숫자 3개로 구성된 모든 세 자리 수를 2차원 배열로 리턴하는 함수
    """
    candidate = [str(i) for i in range(1, 10)]
    combinations = []

    for perm in permutations(candidate, 3):
        combinations.append(list(perm))

    return combinations


def get_strike_and_ball(orig: str, cmp: list or str):
    """
    str/list 형태의 두 숫자를 비교해 strike, ball의 개수를 리턴하는 함수
    strike : 자리와 수가 같을 때 / ball : 자리가 같지 않지만 수를 포함할 때
    """
    strike, ball = 0, 0

    for i in range(3):
        if cmp[i] == orig[i]:
            strike += 1
        else:
            if orig.find(cmp[i]) != -1:
                ball += 1

    return (strike, ball)


def find_proper_answers(
    answers: set, candidates: list, orig: list, strike: int, ball: int
):
    """
    후보군과 original guess를 비교해
    strike, ball의 값이 모두 같으면 answer에 추가,
    같지 않으면 answer에서 제외해 후보를 좁혀가는 함수
    """
    for candidate in candidates:
        all_right, included = get_strike_and_ball(orig, candidate)

        if strike == all_right and ball == included:
            answers.add("".join(candidate))

        else:
            answers.discard("".join(candidate))

    return


for _ in range(int(sys.stdin.readline())):
    guess, strike, ball = sys.stdin.readline().rstrip().split()
    strike, ball = int(strike), int(ball)

    # 모두 맞혔을 때
    if strike == 3:
        print(1)
        exit()

    # answer에 아무것도 없다면, 즉 첫 라운드라면 가능한 모든 조합을 구해 비교
    if not answers:
        candidates = get_all_combinations()
    else:
        candidates = list(answers)

    find_proper_answers(answers, candidates, guess, strike, ball)


print(len(answers))
