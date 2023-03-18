from heapq import heapify, heappush, heappop
# 섞은 음식의 스코빌 지수 = 가장 안 매운 + (두 번째로 가장 안 매운 * 2)
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수 return 

def solution(scoville, K):
    heapify(scoville)
    count = 0
    
    while scoville: 
        last = heappop(scoville)
        
        # 모든 음식의 스코빌 지수가 K 이상
        if last >= K:
            return count
        
        elif len(scoville) < 1:
            return -1
        
        last_second = heappop(scoville)
        
        heappush(scoville, last + (last_second  * 2))
        
        count += 1 
    # return -1

    # return answer

solution([1, 2, 3, 9, 10, 12],7)