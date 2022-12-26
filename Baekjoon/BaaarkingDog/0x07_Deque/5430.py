# AC https://www.acmicpc.net/problem/5430
'''
함수 R : 배열에 있는 수의 순서를 뒤집는 함수
함수 D : 첫 번째 수를 버리는 함수
- 배열이 비어있는데 D를 사용한 경우에는 에러 발생
'''
import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    funcs = sys.stdin.readline().rstrip()
    arr_len = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().strip()[1:-1].split(","))

    if arr_len == 0:
        arr = deque()

    reverse = False #reverse flag
    error = False #error flag

    for func in funcs:
        if func == "R":
            reverse = not reverse

        else:
            if arr:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                error = True
                break
    if error:
        print("error")
        continue

    if reverse:
        arr.reverse()
    
    print('['+','.join(arr)+']')

    

    
