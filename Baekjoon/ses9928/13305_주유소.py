# 주유소 https://www.acmicpc.net/problem/13305

"""
제일 왼쪽의 도시 -> 제일 오른쪽의 도시로 자동차를 이용해 이동
인접한 두 도시 사이의 도로들은 서로 길이가 다를 수 있음

1km = 1l 기름
도로의 길이와 각 도시의 기름값이 주어졌을 때, 최소의 비용 계산
"""

import sys 

city_cnt = int(sys.stdin.readline())

dists = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

# 일단 첫 번째 도시에서는 무조건 주유를 해야 하고, 가장 비용이 낮은 곳에서 주유를 많이 해놓는 게 중요
# min을 찾을 때까지는 그 범위 내에서 가장 작은 도시를 찾아서 그걸로 연명 
# 재귀로 하면 될듯? 
answer = 0

def oil(start: int, end: int, prices: list):
    global answer

    # base case
    if start == end:
        return 
    
    # find minimum price in specific range
    # 마지막 도시에서는 주유를 할 필요가 없으므로 인덱스 end-1까지만 계산

    # 여기에서 비효율이 발생하는 느낌
    min_price = min(prices[start:end])
    idx = prices[start:end].index(min_price)

    answer += sum(dists[idx:end]) * min_price 
    oil(start, idx, prices)


# oil(0, city_cnt-1, prices)

answer = 0
min_cost = prices[0]

for i in range(city_cnt-1):
    if min_cost > prices[i]:
        min_cost = prices[i]
        
    if prices[i] > min_cost:
        prices[i] = min_cost
    
    answer += prices[i] * dists[i]

print(answer)