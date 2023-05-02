# 1, 2, 3 더하기 https://www.acmicpc.net/problem/15989

"""
정수 n이 주어졌을 때, 1, 2, 3의 합으로 나타내는 방법의 수 구하기
"""

import sys 

tc_cnt = int(sys.stdin.readline())
cases = []

for _ in range(tc_cnt):
    cases.append(int(sys.stdin.readline()))

max_num = max(cases)

# 1만 사용해서 만드는 경우는 한 가지
table = [1 for _ in range(max_num + 1)]

# 2를 사용해서 만드는 경우 : table[n-2]개
# 3을 사용해서 만드는 경우 : table[n-3]개 
# 중복을 빼야 하므로 2가 사용되는 경우를 쭉 계산하고, 그 다음에 3이 사용되는 경우를 쭉 계산해야 함
for i in range(2, 4):
    for j in range(i, max_num + 1):
        table[j] += table[j - i]

for case in cases:
    print(table[case])