# 벌집 https://www.acmicpc.net/problem/2292

"""
숫자 n이 주어졌을 때, 벌집 중앙 1에서 n번 방까지 
최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지 계산 
"""

import sys 

n = int(sys.stdin.readline())
# Level 1 : 1 (1개)
# Level 2 : 2 - 7 (6개)
# Level 3 : 8 - 19 (12개)
# Level 4 : 20 - 37 (18개)

i = 1
honey_cnt = 1

while n > honey_cnt:
    honey_cnt += 6 * i
    i += 1
    
    # if n <= 1 + (6 * (i-1)):
    #     print(i)
    #     break
    
    # else:
    #     i += 1

print(i)