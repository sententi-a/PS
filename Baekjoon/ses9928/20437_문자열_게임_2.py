# 문자열 게임 2 https://www.acmicpc.net/problem/20437

"""
- 알파벳 소문자로 이루어진 문자열 W
- 양의 정수 K
- 어떤 문자를 정확히 K개 포함하는 가장 짧은 연속 문자열의 길이 구함
- 어떤 문자를 정확히 K개 포함하고, 문자열의 첫 번째, 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이 구하기
위와 같은 방식으로 게임을 T회 진행
"""

import sys
from collections import defaultdict, Counter

def solution(string, limit):
    scs = 10**4 # 가장 짧은 연속 문자열 (이것도 가장 앞, 뒤 문자가 해당 문자일 때)
    lcs = 0 # 가장 긴 연속 문자열 

    candidates = set()
    counter = Counter(string) # 문자열 내에 각 문자가 몇 번 등장했는지 
    indexes = defaultdict(list) # 문자열 내 각 문자가 어디에 위치하는지 

    # 문자열을 순회하면서 각 문자가 나타난 인덱스를 리스트로 저장
    # 이 때, 특정 문자의 등장 횟수가 K번 이상이면 해당 문자를 시작과 끝으로 하는 substring 후보가 됨
    for i in range(len(string)):
        indexes[string[i]].append(i)
        
        if counter[string[i]] >= limit:
            candidates.add(string[i])

    # 만족하는 연속 문자열이 없을 때 (모든 문자의 개수가 k 이상이 아닐 때)
    if not candidates:
        print(-1)
        return
    
    # scs, lcs의 길이 갱신 (해당 문자가 딱 K번 포함되는 substring의 길이를 모두 구함)
    for char in candidates:
        for i in range(counter[char] - limit + 1):
            length = indexes[char][i + limit - 1] - indexes[char][i] + 1
            if scs > length:
                scs = length
            if lcs < length:
                lcs = length

    print(scs, lcs)
    return

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        string = sys.stdin.readline().rstrip() # 문자열 W 
        limit = int(sys.stdin.readline()) # 정수 K 

        # 정수 k가 1이거나, 문자열 w의 길이가 1이면 답은 무조건 1, 1
        if limit == 1 or len(string) == 1:
            print(1, 1)
            continue

        solution(string, limit)