def solution(n):
    answer = 1
    
    for i in range(1, (n//2)+1) :
        summ = 0
        for j in range(i, (n//2)+2) :
            summ += j
            if summ >= n :
                break
        if summ == n :
            answer += 1
    return answer

"""
처음 문제를 풀었을때 정답은 맞으나 효율성테스트에서 시간초과가 발생했다.
처음에는 summ == n 풀었었는데 summ >= n으로 수정하니 속도가 더 향상될 수 있었고
그 결과 효율성테스트에서도 통과할 수 있었다.
조금 더 효율성을 생각하며 문제를 해결하도록 하자
"""