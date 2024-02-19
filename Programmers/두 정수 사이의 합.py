def solution(a, b):
    answer = 0
    if (a-b) > 0 :
        for i in range(b, a+1) :
            answer += i
    elif (b-a) > 0 :
        for j in range(a, b+1) :
            answer += j
    else :
        answer = a
    return answer