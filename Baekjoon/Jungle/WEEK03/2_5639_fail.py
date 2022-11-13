# 이진 검색 트리 https://www.acmicpc.net/problem/5639

import sys 
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self, val):
        self.val = val
        self.lc = self.rc = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val): 
        def insert_node(node, val):
            if val == node.val: # 값이 트리에 이미 존재한다면 삽입 실패 
                return False
            elif val < node.val: # 값이 현재 주목하고 있는 노드의 값보다 작을 때 (왼쪽)
                if node.lc == None: # 왼쪽 자식이 없다면 바로 왼쪽 자식으로 지정
                    node.lc = Node(val)
                else: # 왼쪽 자식이 있다면 그 노드에서 시작해 다시 탐색
                    insert_node(node.lc, val)
            else: # 값이 현재 주목하고 있는 노드의 값보다 클 때 (오른쪽)
                if node.rc == None:
                    node.rc = Node(val)
                else:
                    insert_node(node.rc, val)
            return True
        
        # root가 없다면 root 노드로 지정
        if self.root == None:
            self.root = Node(val)
            return True
        # root가 있다면 내부 함수인 insert_node()를 루트 노드부터 돌림
        else:
            return insert_node(self.root, val)

    def postorder(self):
        def print_subtree(node):
            if node != None:
                print_subtree(node.lc)
                print_subtree(node.rc)
                print(node.val)
        root = self.root
        print_subtree(root)

# main
case = []

while True:
    try:
        case.append(int(sys.stdin.readline()))
    except:
        break

bst = BinarySearchTree()

for i in range(len(case)):
    bst.insert(case[i])
   
bst.postorder()
