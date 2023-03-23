from collections import deque

def is_adj_word(word_ascii1, word_ascii2):
    temp = [0 for _ in range(len(word_ascii1))]
    for i in range(len(word_ascii1)):
        if abs(word_ascii1[i] - word_ascii2[i]) == 1:
            temp[i] = 1
    if sum(temp) == 1:
        return True
    return False 

def solution(begin, target, words):
    answer = 0
    
    # 변환할 수 없는 경우
    if target not in words:
        return 0
    
    # begin 포함 모든 단어를 ASCII 값으로 변환해 리스트에 저장
    target_ascii = list(map(lambda x: ord(x), target))
    target_index = 0
    words_ascii = [[0, list(map(lambda x: ord(x), begin))]]
    
    for i in range(1, len(words) + 1):
        words_ascii.append([i, list(map(lambda x: ord(x), words[i-1]))])
        if words[i-1] == target:
            target_index = i
            
    # words들의 관계를 인접리스트로 구현하기
    graph = [[] for _ in range(len(words_ascii))]
    for i in range(len(words_ascii)): # 기준
        for j in range(len(words_ascii)): # 비교 대상
            if i == j:
                continue
            if is_adj_word(words_ascii[i][1], words_ascii[j][1]):
                graph[i].append(j)
    
    # BFS 돌리기
    queue = deque([0])
    visited = [False for _ in range(len(words_ascii))]
    
    while queue:
        index = queue.popleft()
        answer += 1
        
        if index == target_index:
            break
        
        for adj in graph[index]:
            if not visited[adj]:
                queue.append(adj)
        
    
    return answer

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])