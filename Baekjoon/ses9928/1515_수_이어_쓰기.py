# 수 이어 쓰기 https://www.acmicpc.net/problem/1515

"""
세준 : 1부터 N까지 모든 수를 차례대로 공백없이 한 줄에 다 씀
다솜 : 마음에 드는 몇 개의 숫자를 지움 (안 지울 수도 있음)

수를 방금 전과 똑같이 쓰려고 하는데, N이 기억나지 않음
남은 수를 이어 붙인 수가 주어질 때, N의 최솟값 구하기 
"""

import sys 

nums = sys.stdin.readline().rstrip()

i = 0

while True:
    i += 1
    num = str(i)

    # i가 문자열에 '포함'될 수 있는지 확인하는 과정
    # i의 모든 자릿수를 비교해야 함! 즉, len(num)이 > 0일 때까지
    # (EX) num = 10 vs nums = 11111 
    # 문자열의 문자가 하나 남았을 때도 고려해야 하므로 len(nums) > 0라는 조건도 붙여야 함 
    while len(num) > 0 and len(nums) > 0:
        if num[0] == nums[0]:
            nums = nums[1:]
        
        num = num[1:]

    if not nums:
        print(i)
        break