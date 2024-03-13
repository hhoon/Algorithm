def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1) :
        cnt = 0
        for j in range(1, int(i**(1/2))+1) :
            if i % j == 0 :
                if j*j == i :
                    cnt += 1
                else :
                    cnt += 2
        if cnt > limit :        
            answer += power
        else :
            answer += cnt
        
    return answer

"""
해당 문제를 풀때 시간초과가 발생하였다
해당 수의 약수를 구할때는 그 수위 제곱근 이상은 시도해볼 필요가 없다고 한다.
ex) 루트18의 경우 4.xxx
18의 약수 : 1 2 3 6 9 18
대칭이기 때문에 1 2 3을 하고 이것을 2배 해주면 약수의 개수를 구할 수 있다.
하지만 36의 약수의 경우 : 1 2 3 4 6 9 12 18 36
가운데 6을 기준으로 대칭이기 때문에 6을 제외하고는 2배를 해주고 6의 경우만 1개로
카운트를 해주면 위와 같이 문제를 해결할 수 있다.
"""