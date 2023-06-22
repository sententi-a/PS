# List of Unique Numbers https://www.acmicpc.net/problem/13144

"""
길이가 N인 수열이 주어질 때, 
수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러 번 등장하지 않는 경우의 수 구하기
"""

import sys 

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split())) + [0]

if n == 1:
    print(1)
    exit()

cnt = 0
start, end = 0, 0
visited = [False for _ in range(max(sequence) + 1)]

while start < n and end < n:
    # start ~ end 까지 중복 숫자가 없다면
    # end 포함 만들 수 있는 수열의 조합 개수를 더함
    if not visited[sequence[end]]:
        visited[sequence[end]] = True
        end += 1
        cnt += (end - start)
    # 중복 숫자가 있다면 앞쪽 포인터를 뒤로 당김
    else:
        visited[sequence[start]] = False
        start += 1

    
print(cnt)