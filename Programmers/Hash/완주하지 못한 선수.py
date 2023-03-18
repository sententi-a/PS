"""마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수 작성."""

from collections import Counter

def solution(participant, completion): 
    print(list(Counter(participant) - Counter(completion))[0])
        
    # answer = ''
    # return answer 

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]	)