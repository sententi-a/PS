# 알파벳 개수 https://acmicpc.net/problem/10808
import sys

word = sys.stdin.readline().rstrip()

for i in range(26):
    count = 0
    for char in word:
        if char == chr(i+97):
            count += 1
    print(count, end=" ")

