# 이진 검색 트리 https://www.acmicpc.net/problem/5639
# 참고 : https://chinpa.tistory.com/17

import sys 
sys.setrecursionlimit(1000000)

def pre_to_post(start, end):
    if start > end:
        return

    root = case[start] # 전위순회로 나온 가장 첫 번째 요소는 항상 root
    division = end + 1

    # 값이 root보다 커지는 분기 찾기
    for i in range(start+1, end+1):
        if root < case[i]:
            division = i
            break
    
    pre_to_post(start+1, division-1) # 왼쪽 subtree
    pre_to_post(division, end) # 오른쪽 subtree
    print(root) # 현재 노드


case = []

while True:
    try:
        case.append(int(sys.stdin.readline()))
    except:
        break

pre_to_post(0, len(case)-1)

