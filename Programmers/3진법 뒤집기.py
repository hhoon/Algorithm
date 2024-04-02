def solution(n):
    answer = ''
    three = []
    while True :
        if n >= 3 :
            three.append(str(n%3))
            n = n // 3
        else :
            three.append(str(n))
            break
            
    for i in three :
        answer += i
        
    answer = int(answer, 3)
    return answer