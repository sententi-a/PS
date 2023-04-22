# 비슷한 단어 https://www.acmicpc.net/problem/2607

"""
1. 두 개의 단어가 같은 종류의 문자로 이루어짐
2. 같은 문자는 같은 개수만큼 있음

- 두 단어가 같은 구성일 경우 
- 한 단어에서 한 문자를 더하거나, 빼거나, 다른 문자로 바꿔 같은 구성을 갖게될 경우 
-> 이 때 두 단어를 서로 비슷한 단어라고 함

첫 번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력
"""

import sys
from collections import Counter

word_cnt = int(sys.stdin.readline())
comp_word = sys.stdin.readline().rstrip()
words = []
answer = 0

for _ in range(word_cnt-1):
    words.append(sys.stdin.readline().rstrip())

comp_word_counter = Counter(comp_word)

for word in words:
    word_counter = Counter(word)
    
    if len(word) >= len(comp_word): 
        diff = word_counter - comp_word_counter
    else:
        diff = comp_word_counter - word_counter

    # 두 단어가 같은 구성일 경우
    if not diff:
        answer += 1
    
    # 한 문자를 더하거나, 빼거나, 다른 문자로 바꿔 같은 구성일 때
    elif len(diff) == 1:
        if list(diff.items())[0][1] == 1:
            answer += 1
   

print(answer)