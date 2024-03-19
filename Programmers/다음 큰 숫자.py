def solution(n):
    answer = 0
    n2 = bin(n) [2:]
    n2_cnt = n2.count('1')
    
    while True :
        n += 1
        next_num = bin(n) [2:]
        if next_num.count('1') == n2_cnt :
            answer = n
            break
    return answer