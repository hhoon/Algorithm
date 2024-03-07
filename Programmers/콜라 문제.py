def solution(a, b, n):
    answer = 0
    
    while True :
        if n < a :
            break
        rest = n%a
        plus = (n//a)*b
        answer += plus
        n = rest + plus
        
    return answer