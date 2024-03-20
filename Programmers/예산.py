def solution(d, budget):
    answer = 0
    d.sort()
    
    while True :
        if sum(d) > budget:
            d.pop()
        else :
            answer = len(d)
            break
    
    return answer