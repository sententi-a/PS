# 가희와 키워드 https://www.acmicpc.net/problem/22233

"""
메모장에 써진 키워드는 총 N개이고, 서로 다름
새로운 글을 작성할 때 최대 10개의 키워드에 대해 글을 작성
블로그에 글을 쓴 후 메모장에 있는 키워드 개수가 몇 개인지 계산하기
- x번째 글을 쓰고 난 후 남아있는 키워드 출력
"""

import sys

keyword_cnt, post_cnt = map(int, sys.stdin.readline().split())

keywords = set()
answers = []

for i in range(keyword_cnt):
    keywords.add(sys.stdin.readline().rstrip())

for i in range(post_cnt):
    words = sys.stdin.readline().rstrip().split(',')

    for word in words:
        keywords.discard(word)
    
    answers.append(len(keywords))

print(*answers, sep="\n")