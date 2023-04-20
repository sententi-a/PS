# 블로그 https://www.acmicpc.net/problem/21921

import sys

day_passed, counting_days = map(int, sys.stdin.readline().split())
visitors = list(map(int, sys.stdin.readline().split()))

# 최대 방문자가 0일 때
max_visitor = max(visitors)

if max_visitor == 0:
    print('SAD')
    exit()

# 1일 동안 가장 많이 들어온 방문자 수를 구할 때
if counting_days == 1:
    print(max_visitor)
    print(1)
    exit()

# 전체 기간 중 가장 많이 들어온 방문자 수를 구할 때
if counting_days == day_passed:
    print(sum(visitors))
    print(counting_days)
    exit()

# 시간 초과 -> X가 25000이고, N이 12500이면 총 연산이 10^10이 넘으므로 시간초과
# 투포인터 사용해서 빼고 더하기 
# 초기값
temp_visitors = sum(visitors[:counting_days])
max_visitors_and_period = [temp_visitors, 1]

for i in range(day_passed - counting_days):
    # print(temp_visitors)
    temp_visitors -= visitors[i]
    temp_visitors += visitors[i+counting_days]
    
    if temp_visitors > max_visitors_and_period[0]:
        max_visitors_and_period[0] = temp_visitors
        max_visitors_and_period[1] = 1

    elif temp_visitors == max_visitors_and_period[0]:
        max_visitors_and_period[1] += 1

print(max_visitors_and_period[0])
print(max_visitors_and_period[1])

