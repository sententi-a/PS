# 비슷한 단어 https://www.acmicpc.net/problem/2179

"""
가장 비슷한 두 단어 구하기
- 두 단어의 접두사 길이로 측정 
- (접두사 길이가 최대인 게 여러 개라면, 입력되는 순서가 앞쪽인 단어가 답)
- 두 단어는 서로 달라야 함
"""

import sys 

def return_max_prefix(a: str, b: str):  
    """
    문자열 a, b의 공통 접미사 길이를 리턴하는 함수
    """
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return i
        
    return min(len(a), len(b))


word_cnt = int(sys.stdin.readline())
words = []

# 인덱스와 함께 단어를 추가한 후, 단어를 사전순으로 정렬
for i in range(word_cnt):
    words.append((sys.stdin.readline().rstrip(), i))

words.sort(key=lambda x:(x[0], x[1]))

max_length = 0
answer = []

# 모든 조합을 비교 (O(n^2))
for i in range(word_cnt):
    for j in range(i+1, word_cnt):
        
        # 가장 첫번째 알파벳이 다르면 그 다음 단어도 모두 다르므로 반복문을 빠져나옴 
        if words[i][0][0] != words[j][0][0]:
            break

        result = return_max_prefix(words[i][0], words[j][0])

        # 인덱스가 작은 게 a, 큰 게 b
        if words[i][1] < words[j][1]:
            a, b = words[i], words[j]
        else:
            a, b = words[j], words[i]

        # 무조건 answer을 갱신해야 하는 경우
        if result > max_length:
            max_length = result
            answer = [a, b]
            
        # 접두사의 길이가 최대인 경우가 여러 개일 때, 제일 앞쪽에 있는 단어를 답으로 함
        elif result == max_length:
            if answer[0][1] > a[1] and answer[1][1] > b[1]:
                answer = [a, b]

# print(words)

for elem in answer:
    print(elem[0])


# TC
# 5
# abab
# abaa
# abcdab
# abcda
# abcdaa
# ---------
# 5
# ae
# ab
# ac
# aa
# ad
# ---------
# 4
# aa
# bb
# bc
# aj

