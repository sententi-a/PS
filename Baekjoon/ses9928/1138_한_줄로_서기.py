# 한 줄로 서기 https://www.acmicpc.net/problem/1138

"""
N명의 사람들이 줄을 섬
자신보다 큰 사람이 왼쪽에 몇 명 있었는지만 기억
각 사람들이 기억하는 정보가 주어질 때, 줄을 어떻게 설지 출력
"""

import sys
from itertools import permutations

ppl_cnt = int(sys.stdin.readline())
ppl = [i for i in range(1, ppl_cnt+1)]

left_higher_people = list(map(int, sys.stdin.readline().split()))

# 1st 시도 : permutations로 모든 경우의 수 구함
# for perm in permutations(ppl, ppl_cnt):
#     flag = True

#     for i in range(ppl_cnt):
#         person = perm[i] 
#         higher_people_cnt = 0
        
#         # 자신보다 키가 큰 사람의 수 구하기
#         for j in range(0, i):
#             if perm[j] > person:
#                 higher_people_cnt += 1

#         # 구한 사람 수가 입력으로 주어진 수와 다를 경우 다음 경우의 수로 넘엉감
#         if higher_people_cnt != left_higher_people[person-1]:
#             flag = False
#             break

#     if flag:
#         print(*perm)
#         exit()
        
o =[] 

for i in left_higher_people[::-1]:
    print(i)
    o.insert(i, ppl_cnt)
    ppl_cnt -= 1
    print(o)
