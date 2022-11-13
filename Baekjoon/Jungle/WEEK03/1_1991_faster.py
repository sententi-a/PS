# 트리 순회 https://www.acmicpc.net/problem/1991

import sys

n = int(sys.stdin.readline())

# 인덱스를 부모로 보고, 그 인덱스의 왼쪽 / 오른쪽 자식을 저장한 리스트 
# (인덱스는 1부터 시작, 자식이 없다면 0)
lc = [0 for _ in range(n+1)] 
rc = [0 for _ in range(n+1)]


for _ in range(n):
    nodes = list(sys.stdin.readline().split())
    i = ord(nodes[0]) - 64
    if nodes[1] != '.':
        lc[i] = ord(nodes[1]) - 64
    if nodes[2] != '.':
        rc[i] = ord(nodes[2]) - 64

def preorder(root: int):
    print(chr(root+64), end="")
    if lc[root] != 0:
        preorder(lc[root])
    if rc[root] != 0:
        preorder(rc[root])


def inorder(root: int):
    if lc[root] != 0:
        inorder(lc[root])
    print(chr(root+64), end="")
    if rc[root] != 0:
        inorder(rc[root])


def postorder(root: int):
    if lc[root] != 0:
        postorder(lc[root])
    if rc[root] != 0:
        postorder(rc[root])
    print(chr(root+64), end="")



preorder(1)
print()
inorder(1)
print()
postorder(1)