# 보물 https://www.acmicpc.net/problem/1026

"""
S = A[0] * B[0] + ... + A[N-1] * B[N-1]
S의 값을 가장 작게 만들기 위해 A의 수를 재배열
단, B에 있는 수는 재배열하면 안 됨
S의 최솟값을 출력하는 프로그램
"""

# 재배열하지 말라고 했지만, A는 오름차순, B는 내림차순으로 정렬하면 됨
import sys

count = int(sys.stdin.readline())
answer = 0

list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))

list_a.sort()
list_b.sort(reverse=True)

for i in range(count):
    answer += list_a[i] * list_b[i]

print(answer)