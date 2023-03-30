# 추월 https://www.acmicpc.net/problem/2002

"""
대근 : 터널 입구, 영식 : 터널 출구

대근 : 차가 터널에 들어가는 순서대로
영식 : 차가 터널에서 나오는 순서대로

N개의 차량이 지나간 후, 차량 번호 목록을 보고 반드시 추월을 했을 것으로 예상되는 차 번호 구하기
단순히 들어온 순서보다 나간 순서가 앞에 있다고 해서 추월 여부를 확인할 수 없음
in: 1 2 3 4 5
out: 1 2 5 4 3
이런 경우에는 4, 5 둘 다 추월한 경우이지만, 4가 count되지 않음

결국 나보다 더 나중에 나간 차들 중 나보다 더 먼저 들어왔던 차가 있는지 확인해야 더 정확히 풀 수 있음
"""

import sys
from collections import defaultdict

car_cnt = int(sys.stdin.readline())
cars_in = defaultdict()
cars_out = []
answer = 0

for i in range(car_cnt):
    cars_in[sys.stdin.readline().rstrip()] = i

for i in range(car_cnt):
    cars_out.append(sys.stdin.readline().rstrip())

for i in range(car_cnt):
    for j in range(i+1, car_cnt):
        # 현재 보고 있는 차가 추월했는지 안했는지
        # 나보다 늦게 나온 차가 사실은 먼저 들어왔는지 체크
        if cars_in[cars_out[i]] > cars_in[cars_out[j]]:
            answer += 1
            break
    # if cars_in[sys.stdin.readline().rstrip()] > j:
        # answer += 1

print(answer)

