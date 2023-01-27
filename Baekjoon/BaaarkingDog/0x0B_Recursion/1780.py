# 종이의 개수 https://www.acmicpc.net/problem/1780

"""
NxN 크기의 종이가 있고, 각 칸에는 -1, 0, 1 중 하나가 저장되어 있음
이 행렬을 규칙에 따라 적절한 크기로 자르려고 함
- 만약 종이가 모두 같은 수로 되어 있다면, 그대로 사용
- 아닌 경우, 종이를 같은 크기의 종이 9개로 자르고, 각각 잘린 종이에 대해 과정 반복

종이를 잘랐을 때 -1로만 채워진 종이 개수, 0으로만 채워진 종이 개수, 1로만 채워진 종이 개수 구하기
"""

import sys
sys.setrecursionlimit(10**6)

paper = [] 
n = int(sys.stdin.readline())
# recursion_flag = False

count_ne = 0 # -1
count_ze = 0 # 0
count_po = 0 # 1

for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

# 인자로 받아야 할 것 : x1, y1, x2, y2 (시작 좌표, 끝 좌표)
def paper_cut(x1, y1, x2, y2):
    global n, count_ne, count_ze, count_po
    
    number = paper[x1][y1] 

    # Base Condition: 길이가 1인 경우
    # if x2 - x1 == 1 or y2 - y1 == 1:
        # if number == -1:
        #     count_ne += 1
        # elif number == 0:
        #     count_ze += 1
        # else:
        #     count_po += 1
        # return
    

    for i in range(x1, x2):
        for j in range(y1, y2):
            # 조건을 생각해보자
            if paper[i][j] != number:
                # 0 - 9 : 0-3, 3-6 6-9
                paper_cut(x1, y1, x2//3, y2//3)
                paper_cut(x1, y2//3, x2//3, y2*2//3)
                paper_cut(x1, y2*2//3, x2//3, y2)

                paper_cut(x2//3, y1, x2*2//3, y2//3)
                paper_cut(x2//3, y2//3, x2*2//3, y2*2//3)
                paper_cut(x2//3, y2*2//3, x2*2//3, y2)

                paper_cut(x2*2//3, y1, x2, y2//3)
                paper_cut(x2*2//3, y2//3, x2, y2*2//3)
                paper_cut(x2*2//3, y2*2//3, x2, y2)
                # return 
    
    if number == -1:
        count_ne += 1

    elif number == 0:
        count_ze += 1
    else:
        count_po += 1
    return 
            

paper_cut(0, 0, n, n)
print(count_ne, count_ze, count_po, sep="\n")