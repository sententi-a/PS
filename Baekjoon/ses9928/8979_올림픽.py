# 올림픽 https://www.acmicpc.net/problem/8979

"""
1. 금메달 수가 더 많은 나라
2. 은메달 수가 더 많은 나라
3. 동메달 수가 더 많은 나라 
+ 모든 메달의 수가 같을 경우 공동 순위
순서대로 어느 나라가 더 높은 순위인지 결정

각 국가는 1부터 n 사이 정수로 표현,
한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의 
""" 

import sys
from collections import defaultdict

country_cnt, target_country = map(int, sys.stdin.readline().split())
countries = []

for _ in range(country_cnt):
    countries.append(list(map(int, sys.stdin.readline().split())))

countries.sort(key= lambda x: (-x[1], -x[2], -x[3]))
ranking = defaultdict()

# for i in range(len(countries)):
#     if countries[i][0] == target_country:
#         print(i)

i = 0
rank = 1

while i < country_cnt:
    same_rank_count = 1
    # ranking[rank].add(countries[i][0])
    ranking[countries[i][0]] = rank

    while i < country_cnt - 1 and countries[i][1] == countries[i+1][1] and countries[i][2] == countries[i+1][2] and countries[i][3] == countries[i+1][3]:
        # ranking[rank].add(countries[i+1][0])
        ranking[countries[i+1][0]] = rank
        same_rank_count += 1
        i += 1

    i += 1
    rank += same_rank_count
    
print(ranking[target_country])
