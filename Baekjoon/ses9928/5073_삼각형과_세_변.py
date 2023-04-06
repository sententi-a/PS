# 삼각형과 세 변 https://www.acmicpc.net/problem/5073

"""
Equilateral : 세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우

가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 Invalid 
"""

import sys 

while True:
    num1, num2, num3 = map(int, sys.stdin.readline().split())

    if num1 == 0:
        exit() 

    nums = [num1, num2, num3]
    nums.sort(reverse=True)

    if nums[0] >= nums[1] + nums[2]:
        print('Invalid')

    else:
        if num1 == num2 and num2 == num3:
            print("Equilateral")
        
        elif num1 == num2 or num2 == num3 or num3 == num1:
            print("Isosceles")
        
        else:
            print("Scalene") 

