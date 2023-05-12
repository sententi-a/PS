# 숨바꼭질 3 https://www.acmicpc.net/problem/13549

"""
수빈 : 점 N
동생 : 점 K 

수빈이는 걷거나 순간이동을 할 수 있음
- 걷는다 : 1초 후 X-1 / X+1로 이동 
- 순간이동한다 : 0초 후 2 * X로 이동

수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초 후인지 구하기
"""

import sys

subin, sister = map(int, sys.stdin.readline().split())

# DP
# 최솟값 찾기는 subin의 위치부터 시작하고, 이 위치보다 더 작은 곳들은 subin과의 거리가 최솟값임

INF = 10 ** 6

# 동생의 위치가 수빈보다 작을 때는 바로 출력 
if sister <= subin:
    print(subin - sister) 
    exit()

times = [INF for _ in range(max(subin, sister) + 2)]

# 생각해보니, subin이 0이어도 뒤에서 DP 테이블을 채울 때 times[pos-1] + 1로 최솟값 갱신되므로 굳이 거칠 필요 없는 과정
# 수빈이의 위치가 0일 때는 무조건 1에서 출발한다고 생각하고 1까지 가는 최소 시간 갱신 
# if subin == 0:
#     times[1] = 1

# 수빈보다 작거나 같은 위치에 있는 곳들 
for pos in range(0, subin + 1):
    times[pos] = subin - pos

# 아래 DP 테이블에 값 넣는 로직에서 다시 확인하므로 필요 없는 과정
# 수빈이의 위치 기준 *2, *4, *8 ... 을 모두 0으로 만듦
# if subin != 0:
#     idx = subin

#     while idx <= sister:
#         times[idx] = times[subin]
#         idx *= 2

for pos in range(subin + 1, sister + 1):
    if pos % 2 == 0:
        times[pos] = min(times[pos], times[pos-1] + 1, times[pos + 1] + 1, times[pos // 2])
    else:
        times[pos] = min(times[pos], times[pos-1] + 1, times[pos+1] + 1, times[(pos-1) // 2] + 1, times[(pos+1) // 2] + 1)

    # 어차피 뒤에서 다시 확인하기 때문에 필요 없는 과정
    # idx = pos

    # while idx <= sister:
    #     times[idx] = times[pos]
    #     idx *= 2
    
print(times[sister])