def solution(arr):
    answer = []
    minn = min(arr)
    if len(arr) == 1 :
        answer.append(-1)
        return answer
    else :
        for i in arr :
            if i != minn :
                answer.append(i)
        return answer