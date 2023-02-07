# 부분수열의 합 https://acmicpc.net/problem/1182
"""
N개의 정수로 이루어진 수열이 있을 때, 
크기가 양수인 부분수열 중 
그 수열의 원소를 다 더한 값이 S가 되는 경우의 수 구하기
1<=N<=20, |S|<=1,000,000
"""
import sys

n, goal = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
result = []
count = 0 # 조건을 만족하는 부분수열의 개수 

# 수열의 각 원소를 더할지 말지 선택
def sol(cur, total):
    global goal, n, count

    # 수열을 다 돌아서 선택했고, 부분수열의 합이 goal이라면 
    if cur == n:
        if total == goal:
            count += 1
        return 

    # 현재 보고 있는 원소를 고르지 않았을 때
    sol(cur+1, total)
    # 현재 보고 있는 원소를 골랐을 때 
    sol(cur+1, total+sequence[cur])


sol(0, 0)
if goal == 0:
    count -= 1
print(count)