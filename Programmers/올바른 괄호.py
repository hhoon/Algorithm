def solution(s):
    answer = True
    cnt1 = 0
    cnt2 = 0
    
    for i in s :
        if cnt2 > cnt1 :
            answer = False
            break
        else :
            if i == '(' :
                cnt1 += 1
            else :
                cnt2 += 1
    if cnt1 != cnt2 :
        answer = False
        
    return answer

"""
괄호를 각각 cnt하고 ')'가 더 많은 경우와 cnt1과 cnt2를 비교하는 방법으로 문제를
해결할 수 있다.
"""