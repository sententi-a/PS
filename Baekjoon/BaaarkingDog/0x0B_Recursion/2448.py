# 별 찍기 - 11 https://acmicpc.net/problem/2448
"""
n은 항상 3*2^k 수 (0 <= k <= 10)
규칙을 보고 유추한 뒤에 별 찍어보기

           * 
          * *
         *****
        *     *
       * *   * *
      ***** *****
     *           * 
    * *         * *
   *****       *****
  *     *     *     *
 * *   * *   * *   * *
***** ***** ***** *****
"""
import sys
from math import log

case = int(sys.stdin.readline())

answer = [[' ' for _ in range(2*case-1)] for _ in range(case)]

def star(x, y, n):
    """
    1, 3, 5, 7, 9, (2*n - 1)
    """
    # Base condition
    if n == 3:
        # 첫 번째 줄 
        answer[x][y+2] = '*'
        # 두 번째 줄
        answer[x+1][y+1] = '*'
        answer[x+1][y+3] = '*'
        # 세 번째 줄
        for j in range(y, y+2*3-1):
            answer[x+2][j] = '*'
        return
    
    # k = int(log(n//3, 2))

    # star(x, y+3*(2**(k-1)), n//2)
    # star(x+3*(2**(k-1)), y, n//2)
    # star(x+3*(2**(k-1)), y+3*(2**k), n//2)

    star(x, y+n//2, n//2)
    star(x+n//2, y, n//2)
    star(x+n//2, y+n, n//2)

    """
    n == 3 : 트리 1개 
    n == 6 : 트리 3개 
    n == 12 : 트리 9개 
    n == 24 : 트리 27개
    (n*3)*2^k일 때 트리 개수 : 3^k개

         star(3)
    star(3) star(3)
    
         star(6)
    star(6) star(6)

    그러면 각 트리의 시작점만 구하자

    1) n == 6일 때
    (0, 3) => (x, y+3*(2**(k-1)))
    (3, 0) => (x+3*(2**(k-1)), y)
    (3, 6) => (x+3*(2**(k-1)), y+3*(2**k))

    2) n == 12일 때 
    (0, 6) 
    - (3, 6)
    - (3, 12)

    (6, 0)
    - (12, 0)
    - (12, 6)
    
    (6, 12)
    - (12, 12)
    - (12, 18)
    """


star(0, 0, case)

for a in answer:
    print("".join(a))
    
    # 아래는 Timeout
    # print(*a, sep="") 

