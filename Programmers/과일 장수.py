def solution(k, m, score):
    answer = 0
    box = []
    box_cnt = len(score) // m
    tmp = []
    
    score.sort()
    score.reverse()

    if len(score) < m :
        answer = 0
    else :
        for i in range(len(score)) :
            if len(box) == box_cnt :
                break
            else :
                tmp.append(score[i])
                if len(tmp) == m :
                    box.append(tmp)
                    tmp = []
                    
        for i in box :
            minn = min(i)
            answer += (minn * m)
        
    return answer