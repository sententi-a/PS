# 알파벳 개수 https://acmicpc.net/problem/10808

"""
각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램
"""
import sys 

freq = [0 for _ in range(26)] # 문자열에서 a~z까지 각 알파벳이 몇 번 나왔는지 담는 배열

str = sys.stdin.readline().rstrip() # test case

for char in str:
    freq[ord(char)-ord('a')] += 1

print(*freq)