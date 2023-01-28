# 종이의 개수 https://www.acmicpc.net/problem/1780

"""
NxN 크기의 종이가 있고, 각 칸에는 -1, 0, 1 중 하나가 저장되어 있음
이 행렬을 규칙에 따라 적절한 크기로 자르려고 함
- 만약 종이가 모두 같은 수로 되어 있다면, 그대로 사용
- 아닌 경우, 종이를 같은 크기의 종이 9개로 자르고, 각각 잘린 종이에 대해 과정 반복

종이를 잘랐을 때 -1로만 채워진 종이 개수, 0으로만 채워진 종이 개수, 1로만 채워진 종이 개수 구하기
"""

import sys

paper = [] 
n = int(sys.stdin.readline())

for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

answer = {-1: 0, 0: 0, 1: 0}

# 인자로 받아야 할 것 : x1, y1, x2, y2 (시작 좌표, 끝 좌표)
def paper_cut(x, y, length):
    
    number = paper[x][y] # 종이 시작점의 숫자
    
    for i in range(x, x + length):
        for j in range(y, y + length):
            if paper[i][j] != number:
                div_len = length // 3

                paper_cut(x, y, div_len)
                paper_cut(x, y+div_len, div_len)
                paper_cut(x, y+(2*div_len), div_len)

                paper_cut(x+div_len, y, div_len)
                paper_cut(x+div_len, y+div_len, div_len)
                paper_cut(x+div_len, y+(2*div_len), div_len)

                paper_cut(x+(2*div_len), y, div_len)
                paper_cut(x+(2*div_len), y+div_len, div_len)
                paper_cut(x+(2*div_len), y+(2*div_len), div_len)
                return 
    
    # Base condition : 길이 1이거나 행렬 내 모든 원소가 같은 숫자
    answer[number] += 1
    return

paper_cut(0, 0, n)

for a in answer:
    print(answer[a])

# dfs 재귀