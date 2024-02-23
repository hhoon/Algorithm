def solution(s):
    answer = True
    p = s.count("p")
    P = s.count("P")
    y = s.count("y")
    Y = s.count("Y")
    p_cnt = p + P
    y_cnt = y + Y
    
    if p_cnt != y_cnt :
        answer = False
    else :
        True
        
    return answer