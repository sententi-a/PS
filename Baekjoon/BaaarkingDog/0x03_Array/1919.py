# 애너그램 만들기 https://acmicpc.net/problem/1919

"""
두 영어 단어가 철자의 순서를 뒤바꾸어 같아질 수 있을 때, 서로 애너그램 관계에 있다고 함
두 개의 영단어가 주어졌을 때 애너그램 관계에 있도록 만들기 위해 제거해야 하는 문자 수를 구해보시오
(* 문자 제거시 아무 위치에 있는 문자든지 제거할 수 있음)
(* 두 개의 단어가 순서를 뒤집지 않아도 같다면 애너그램 관계에 있다고 침)
"""

import sys

word1 = list(sys.stdin.readline().rstrip())
word2 = list(sys.stdin.readline().rstrip())

def make_anagram(str1, str2):
    count = 0

    for i in range(len(str1)-1, -1, -1):
        if str1.count(str1[i]) > str2.count(str1[i]):
            del str1[i]
            count += 1
    
    for i in range(len(str2)-1, -1, -1):
        if str2.count(str2[i]) > str1.count(str2[i]):
            del str2[i]
            count += 1
  
    print(count)
    return


make_anagram(word1, word2)