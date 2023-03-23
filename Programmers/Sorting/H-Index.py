# h번 이상 인용된 논문이 h편 이상, 나머지 논문이 h번 이하 인용 (h의 최댓값)
# 무조건 citations 내의 원소값이 아님

def solution(citations):
    n = len(citations)
    answer = n
    
    # citations.sort(reverse=True)
    citations.sort()

    for i in range(n):
        candidate = citations[i]
        if candidate <= n-i:
            answer = candidate

            if i+1 < n and  candidate < n-i <= citations[i+1]:
                answer = n-i-1
    
    print(answer)
    return answer

solution([0, 1, 3, 5, 6])
solution([10000, 10000, 999])
solution([10000 for _ in range(1001)])
solution([1, 1, 1, 1, 1, 1])
solution([3, 3, 7, 7, 7, 7])
solution([3, 3, 3, 3, 4, 7])
