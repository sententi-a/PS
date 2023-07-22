# 어려운 소인수분해 https://www.acmicpc.net/problem/16563

"""
자연수 N개 소인수분해하기
(1 <= N <= 1,000,000)
"""

import sys

MAX_NUM = round(5 * (10**6))


def get_min_prime_nums(n: int):
    min_prime_nums = [i for i in range(n + 1)]

    for i in range(2, int(n**0.5) + 1):
        if min_prime_nums[i] == i:  # 소수라면
            for j in range(2 * i, n + 1, i):  # 아직 소수 최솟값을 안 구했다면
                if min_prime_nums[j] == j:
                    min_prime_nums[j] = i

    return min_prime_nums


def find_dividends(num: int, min_prime_nums: list):
    result = []

    while num > 1:
        result.append(min_prime_nums[num])
        num //= min_prime_nums[num]

    return result


if __name__ == "__main__":
    num_cnt = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    min_prime_nums = get_min_prime_nums(max(nums))
    answers = []

    for num in nums:
        answers.append(find_dividends(num, min_prime_nums))

    for i in range(num_cnt):
        print(*answers[i], sep=" ")
