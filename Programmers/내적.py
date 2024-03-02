def solution(a, b):
    answer = 0
    for i in range(len(a)) :
        ab = a[i]*b[i]
        answer += ab
    return answer