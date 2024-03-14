def solution(n):
    answer = 0
    for i in range(2,n+1) :
        cnt = 0
        if i == 2 or i == 3:
            answer += 1
        else :
            for j in range(2, int(i**(1/2))+1) :
                if i % j == 0 :
                    cnt += 1
                    break
            if cnt == 0 :
                answer += 1
            
    return answer

"""
소수를 찾는것도 약수를 찾는것과 같이 제곱근까지만 확인해보면 소수를 판별할 수 있다고 한다.
이를 활용하면 문제를 해결할 수 있다.
"""