# 인쇄 대기 목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냄
# 나머지 인쇄 대기 목록에서 J보다 중요도가 높은 문서(클수록 중요)가 한 개라도 존재하면 J를 마지막으로 넣음
# 그렇지 않으면 J 인쇄
# location : 내가 인쇄를 요청한 문서가 몇 번째인지
# 이 문서가 몇 번째로 인쇄되는지 return

from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(enumerate(priorities))
    # queue = 
    
    while priorities:
        doc = priorities.popleft()
        
        print(doc)
        if priorities: 
            if doc[1] >= max(priorities, key=lambda x: x[1])[1]:
                answer += 1
                if doc[0] == location: 
                    break
            else:
                 priorities.append(doc)  
        # 반례 : [1, 1, 1, 2], 2
        # target 문서가 마지막에 빠지면 그 값을 계산해줘야 함 
        else:
            answer+=1

    print(answer)
    return answer

solution([1, 1, 1, 2], 2)