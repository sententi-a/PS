# 연산자 끼워넣기 https://www.acmicpc.net/problem/14888
# 백트래킹, DFS
 
import sys 

n = int(sys.stdin.readline()) # 수의 개수 
nums = list(map(int, sys.stdin.readline().split())) # 정수 리스트 
op = list(map(int, sys.stdin.readline().split())) # 연산자 (+, -, * // 순서)

max_res = -(10 ** 9) # -1e9
min_res = 10 ** 9 # 1e9

def dfs(idx, total, add, sub, mul, div): 
    global n, max_res, min_res
    if idx == n:
        max_res = max(max_res, total)
        min_res = min(min_res, total)

    # 연산자 중 어떤 것부터 선택해 연산을 시작할 지 정함 (그래서 elif가 아니고 if)
    if add: 
        dfs(idx+1, total+nums[idx], add-1, sub, mul, div)  
    if sub:
        dfs(idx+1, total-nums[idx], add, sub-1, mul, div)
    if mul:
        dfs(idx+1, total*nums[idx], add, sub, mul-1, div)
    if div:
        dfs(idx+1, int(total/nums[idx]), add, sub, mul, div-1)

dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(max_res)
print(min_res)