from collections import deque
from math import ceil

def solution(progresses, speeds):
    # progresses : 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 (FIFO)
    # speeds : 각 작업의 개발 속도가 적힌 정수 배열
    # 각 배포마다 몇 개의 기능이 배포되는지 리턴
    # info = list(enumerate(list(map(list, zip(progresses, speeds)))))
    
    complete = deque()
    
    for i in range(len(progresses)):
        complete.append([i, ceil((100-progresses[i]) / speeds[i])])
    
    # complete가 [5, 3, 4] 일 경우?

    answer = []      
            
    for i in range(len(complete)):

        if not complete:
            break
        count = 1
        prev_value = complete.popleft()

        while complete and prev_value[0] < complete[0][0] and prev_value[1] >= complete[0][1]:   
            count += 1
            complete.popleft()

        answer.append(count)
            
    return answer


print(solution([1, 1, 50],[100,2, 1]))