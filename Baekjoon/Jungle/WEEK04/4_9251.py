# LCS (Longest Common Subsequence) https://www.acmicpc.net/problem/9251

import sys 

case1 = sys.stdin.readline().rstrip()
case2 = sys.stdin.readline().rstrip()

# case1[-1] == case2[-1] : len(lcs[n][m]) == len(lcs[n-1][m-1]) + 1
# case1[-1] != case2[-1] and lcs[-1] != case1[-1] : case1[:n-1], case2[:m]까지의 LCS가 됨 
# case1[-1] != case2[-1] and lcs[-1] != case2[-1] : case1[:n], case2[:m-1]까지의 LCS가 됨

lcs = [[0 for _ in range(len(case2)+1)] for _ in range(len(case1)+1)] # lcs[i][j] == case1[:i], case2[:j]까지의 LCS 개수

for i in range(len(case1)+1):
    lcs[i][0] = 0
for j in range(len(case2)+1):
    lcs[0][j] = 0

for i in range(1, len(case1)+1):
    for j in range(1, len(case2)+1):
        if case1[i-1] == case2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]) 

print(lcs[len(case1)][len(case2)])

