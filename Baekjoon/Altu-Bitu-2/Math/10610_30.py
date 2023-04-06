# 30 https://www.acmicpc.net/problem/10610

"""
양수 N에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만듦
"""

import sys 
from itertools import permutations

n = str(sys.stdin.readline().rstrip())
nums = list(n)

# 30의 배수이기 때문에 마지막 숫자는 무조건 0이어야 함
nums.sort(reverse=True)

if nums[-1] != '0':
    print(-1)
    exit()

nums.pop()

# permutation 때문에 시간초과
# for perm in permutations(nums, len(nums)):
#     # 가장 앞 숫자가 0이면 안 됨
#     if perm[0] == '0':
#         continue
    
# number = int("".join(nums))

# if number % 3 == 0:
#     print(number, 0, sep='')
# else:
#     print(-1)


# 3의 배수의 특징 : 모든 자리수의 합이 3의 배수임
number = sum(list(map(int, nums)))

if number % 3 == 0:
    print(''.join(nums), 0, sep="")
else:
    print(-1)