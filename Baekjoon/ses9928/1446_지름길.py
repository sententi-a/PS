# 지름길 https://www.acmicpc.net/problem/1446

"""
D킬로미터 길이의 고속도로
모든 지름길은 일방통행이고, 고속도로를 역주행할 수 없음 
운전해야 하는 거리의 최솟값 구하기
"""

import sys 

shortcut_cnt, highway_dist = map(int, sys.stdin.readline().split())
shortcuts = [] 
dists = [i for i in range(highway_dist + 1)]

# [지름길 시작 위치, 도착 위치, 지름길의 길이] 
for _ in range(shortcut_cnt):
    shortcuts.append(list(map(int, sys.stdin.readline().split())))

# # 이전 값을 기준으로 최솟값을 구하기 때문에
# # 도착 위치를 기준으로 오름차순 정렬해야 함 
# shortcuts.sort(key=lambda x: (x[1]))

# # 최소 거리를 갱신하면, 그 뒤에 있는 모든 거리 모두 갱신해줘야 함 
# for shortcut in shortcuts:
#     start, end, dist = shortcut

#     # 지름길 도착 지점이 타겟 거리보다 크면
#     if end > highway_dist:
#         continue
    
#     temp = dists[start] + dist 

#     # 최소 거리 갱신 
#     if dists[end] > temp:
#         dists[end] = temp
#         # 뒤에 있는 모든 거리 갱신
#         for i in range(end + 1, highway_dist + 1):
#             dists[i] = dists[end] + i - end
        
#     # print(dists[:end], end)

# print(dists[highway_dist])

#----------더 효율적인 풀이-----------#
for i in range(highway_dist+1):
    dists[i] = min(dists[i-1]+1, dists[i])
    for start, end, shortcut in shortcuts:
        if i == start and end <= highway_dist and dists[i]+shortcut < dists[end]:
            dists[end] = dists[i]+shortcut
print(dists[highway_dist])
#---------------------------------#