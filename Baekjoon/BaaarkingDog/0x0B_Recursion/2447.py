# 별 찍기 - 10 https://acmicpc.net/problem/2447

"""
n이 3의 거듭제곱이라고 할 때, 크기 n의 패턴은 n*n 정사각형 모양
크기 3의 패턴은 가운데에 공백이 있고, 가운데 제외 모든 칸에 별이 하나씩

n이 3보다 클 경우, 크기 n의 패턴은 공백으로 채워진 가운데의 
(n/3)*(n/3) 정사각형을 크기 n/3 패턴으로 둘러싼 형태

*********
* ** ** *
*********
***   ***
* *   * *
***   ***
*********
* ** ** *
*********
"""

import sys

num = int(sys.stdin.readline())
answer = [[' 'for _ in range(num)] for _ in range(num)]
base = ''

def star(x, y, n):

    if n == 3:
        # base.join('***\n* *\n***')

        for i in range(x, x+3):
            for j in range(y, y+3):
                if i == x + 1 and j == y + 1:
                    continue
                answer[i][j] = '*'
        return
        

    divlen = n // 3

    # 첫 줄 
    for i_1 in range(x, x+divlen, divlen):
        for j_1 in range(y, y+divlen, divlen):
            star(i_1, j_1, divlen)
        for j_2 in range(y+divlen, y+(2*divlen), divlen):
            star(i_1, j_2, divlen)
        for j_3 in range(y+(2*divlen), y+n, divlen):
            star(i_1, j_3, divlen)

    # 두 번째 줄
    for i_2 in range(x+divlen, x+(2*divlen), divlen):
        for j_1 in range(y, y+divlen, divlen):
            star(i_2, j_1, divlen)
        # for j_2 in range(y+divlen, y+(2*divlen), divlen):
        #     star(i_1, j_2, divlen)
        for j_3 in range(y+(2*divlen), y+n, divlen):
            star(i_2, j_3, divlen)

    # 세 번째 줄
    for i_3 in range(x+(2*divlen), x+n, divlen):
        for j_1 in range(y, y+divlen, divlen):
            star(i_3, j_1, divlen)
        for j_2 in range(y+divlen, y+(2*divlen), divlen):
            star(i_3, j_2, divlen)
        for j_3 in range(y+(2*divlen), y+n, divlen):
            star(i_3, j_3, divlen)
    
    """
    star(9)star(9)star(9)
    star(9).......star(9)
    star(9)star(9)star(9)

    star(3)star(3)star(3)
    star(3).......star(3)
    star(3)star(3)star(3)
    """

star(0, 0, num)

for stars in answer:
    print(*stars, sep="")