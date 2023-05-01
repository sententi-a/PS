# 겹치는 건 싫어 https://www.acmicpc.net/problem/20922

"""
같은 원소가 K개 이하로 들어있는 최장 연속 부분 수열의 길이 구하기
"""

import sys 
from collections import Counter

elem_cnt, same_num_limit = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

#------1st 시도 : Brute Force.. 시간 초과------#
# max_length = 0

# for i in range(elem_cnt):
#     for j in range(elem_cnt - 1, i, -1):
#         counter = Counter(nums[i : j + 1])

#         if j - i + 1 <= max_length:
#             break

#         if counter.most_common(1)[0][1] <= same_num_limit:
#             max_length = j - i + 1
#             break

# print(max_length)
#-------------------------------------------#


#--------2nd 시도 : 투 포인터.. 시간 초과--------#
max_length = 0

start, end = 0, 1
num_counter = Counter(nums[:1])

while end < elem_cnt:
    # print(start, end, max_length, num_counter)
    
    # 조건을 만족하지 않으면, 앞의 포인터를 뒤로 밂
    if not (num_counter[nums[end]] < same_num_limit):
        num_counter[nums[start]] -= 1
        start += 1

    # 조건을 만족하면, 뒤의 포인터를 뒤로 밂
    else:
        num_counter[nums[end]] += 1
        end += 1

    # max_length 갱신
    if max_length < end - start:
        max_length = end - start

    
print(max_length)
#------------------------------------------#