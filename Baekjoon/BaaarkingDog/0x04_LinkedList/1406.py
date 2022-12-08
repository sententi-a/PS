# 에디터 https://acmicpc.net/problem/1406

"""
한 줄로된 간단한 에디터! 영어 소문자만 기록할 수 있고, 최대 600,000글자까지 입력 가능
길이가 L인 문자열이 현재 편집기에 입력되어 있다면, 커서가 위치할 수 있는 곳은 L+1 가지

[명령어]
L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨) 
    삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함

모든 명령어를 수행하고 난 뒤 편집기에 입력된 문자열을 출력
"""

import sys 

########################initialize########################
MAX = 10**6 # 최대 입력할 수 있는 글자수
#MAX = 600002

data = [-1 for _ in range(MAX)]
prev = [-1 for _ in range(MAX)]
nxt = [-1 for _ in range(MAX)]

initial_str = sys.stdin.readline().rstrip() # 초기 문자열
cursor = len(initial_str) # 커서 위치 (초기에는 문자열의 맨 뒤에 위치)
unused = cursor + 1 # 새로운 원소가 들어갈 수 있는 인덱스

for i in range(1, len(initial_str) + 1):
    data[i] = initial_str[i-1]
    prev[i] = i-1
    if i != len(initial_str):
        nxt[i] = i+1
nxt[0] = 1 # dummy node의 nxt는 가장 첫 번째 문자의 주소로 설정
##########################################################

def left_move():
    global cursor

    if prev[cursor] != -1:
        cursor = prev[cursor]
    
def right_move():
    global cursor

    if nxt[cursor] != -1:
        cursor = nxt[cursor]


def erase():
    global unused, cursor

    if cursor <= 0:
        return 

    # print(f"지울 데이터 : {data[cursor]}, 커서 위치 {cursor}")

    nxt[prev[cursor]] = nxt[cursor]
    if nxt[cursor] != -1:
        prev[nxt[cursor]] = prev[cursor]

    cursor = prev[cursor]

def insert(char):
    global unused, cursor

    data[unused] = char
    prev[unused] = cursor
    nxt[unused] = nxt[cursor]
    if nxt[cursor] != -1:
        prev[nxt[cursor]] = unused
    nxt[cursor] = unused

    # print(f"넣을 데이터 : {data[unused]}, 커서 위치 : {cursor}")

    unused += 1
    cursor = nxt[cursor]

    
m = int(sys.stdin.readline()) # 명령어의 개수 

for _ in range(m):
    request = list(sys.stdin.readline().split())

    if request[0] == 'L':
        left_move()
    elif request[0] == 'D':
        right_move()
    elif request[0] == 'B':
        erase()
    else:
        insert(request[1])


cur = nxt[0]

while cur != -1:
    print(data[cur], end="")
    cur = nxt[cur]
