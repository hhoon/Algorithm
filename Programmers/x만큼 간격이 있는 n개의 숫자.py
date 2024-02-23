def solution(x, n):
    answer = []
    if x > 0 :
        for i in range(x, (x*n)+1, x) :
            answer.append(i)
    else :
        for j in range(x, (x*n)-1, x) :
            answer.append(j)
    return answer
print(solution(-4,2))