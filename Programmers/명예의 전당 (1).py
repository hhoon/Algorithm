from collections import deque

def solution(k, score):
    answer = []
    rank = []
    for i in range(len(score)) :
        if i <= k-1 :
            rank.append(score[i])
        else :
            rank.sort()
            if score[i] > rank[0] :
                rank = deque(rank)
                rank.popleft()
                rank.appendleft(score[i])
                rank = list(rank)
        answer.append(min(rank))
                
    return answer