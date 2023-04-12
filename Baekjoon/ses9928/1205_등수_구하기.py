# 등수 구하기 https://www.acmicpc.net/problem/1205

"""
게임할 때마다 얻는 점수가 내림차순으로 저장됨
위에서부터 몇 번째 있는 점수인지로 결정 (등수 중복 허용)

태수의 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하기
랭킹 리스트가 꽉 찼을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수 바뀜
"""

import sys

curr_scores_cnt, new_score, max_cnt = map(int, sys.stdin.readline().split())

# 보드에 점수가 없을 때 
if curr_scores_cnt == 0:
    print(1)
    exit()


scores = list(map(int, sys.stdin.readline().split()))
idx = 0

# 점수판이 다 차있고, 새로운 점수가 점수판의 가장 낮은 점수보다도 작거나 같을 때
if scores[-1] >= new_score:
    if max_cnt == curr_scores_cnt:
        print(-1)
        exit()
    else:
        # 3 30 4\n40 30 30의 경우 답이 2가 나와야 함!
        # 따라서 scores[-1] > new_score일 때에만 바로 마지막 순위 출력하게 만듦
        if scores[-1] > new_score:
            print(curr_scores_cnt + 1)
            exit()

for i in range(len(scores)):
    if scores[i] > new_score:
        idx += 1
    else:
        idx += 1
        break

print(idx)