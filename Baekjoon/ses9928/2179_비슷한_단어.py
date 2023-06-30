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
    length = len(a) if len(a) <= len(b) else len(b)
    
    for i in range(length):
        if a[i] != b[i]:
            return i
        
    return length


def update_answer(a: str, b: str, max_length: int):
    """
    문자열 a, b의 공통 접미사의 길이가 max_length 보다 크면 해당 길이를 리턴하고,
    아니라면 원래 max_length 값을 리턴하는 함수
    """
    if a != b:
        result = return_max_prefix(a, b)

        if max_length < result:
            return result
    
    return max_length


word_cnt = int(sys.stdin.readline())
words = []

# 인덱스와 함께 단어를 추가한 후, 단어를 사전순으로 정렬
for i in range(word_cnt):
    words.append((sys.stdin.readline().rstrip(), i))

words.sort(key=lambda x:(x[0], x[1]))

max_length = 0
answer = []

# 앞, 뒤 단어들을 모두 비교
for i in range(word_cnt):
    prev = i - 1

    if 0 <= prev < word_cnt:
        
        result = update_answer(words[prev][0], words[i][0], max_length)
        
        if max_length != result:
            max_length = result
            answer = [words[prev], words[i]]

    nxt = i + 1

    if 0 <= nxt < word_cnt:
        result = update_answer(words[i][0], words[nxt][0], max_length)

        if max_length != result:
            max_length = result
            answer = [words[i], words[nxt]]
      
print(words)
answer.sort(key=lambda x: x[1])

for elem in answer:
    print(elem[0])