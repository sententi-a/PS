# 단어 공부 https://www.acmicpc.net/problem/1157

import sys
from collections import Counter

word = sys.stdin.readline().rstrip().upper()

counter = Counter(word).most_common(2)

if len(counter) == 2 and counter[0][1] == counter[1][1]:
    print("?")
          
else:
    print(counter[0][0])