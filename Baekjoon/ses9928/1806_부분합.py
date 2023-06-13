# 부분합 https://www.acmicpc.net/problem/1806

"""
10,000 이하의 자연수로 이루어진 길이 N짜리 수열에서 
연속된 수들 중 부분합이 S 이상이 되는 것 중 가장 짧은 것의 길이 구하기 
"""

import sys 

n, lower_limit = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split())) + [0]
 
# 합을 만드는 것이 불가능하다면 0 출력
if sum(sequence) < lower_limit:
    print(0)
    exit()

partial_sum = sequence[0]
end = 1
length = 1
answer = 10 ** 10

for start in range(n):
    # 길이가 1일 때가 최소이므로 바로 반복문을 빠져나옴 
    if sequence[start] >= lower_limit:
        answer = 1
        break
    
    # end == n가 될 경우, end - start + 1이 제대로된 길이를 나타내지 않음
    # 따라서, 길이를 관리하는 변수를 두는 것이 정답
    while partial_sum < lower_limit and end < n:
        partial_sum += sequence[end]
        end += 1
        length += 1

    if partial_sum >= lower_limit:
        if length < answer:
            answer = length
    
    partial_sum -= sequence[start]
    length -= 1

print(answer)