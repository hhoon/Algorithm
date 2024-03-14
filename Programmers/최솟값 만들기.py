def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    B.reverse()
    for i in range(len(A)) :
        answer += (A[i] * B[i])
    return answer

"""
작은수와 큰수를 곱한 후 더해야 최솟값을 가질수 있기 때문에 위와 같이 sort()와 reverse()를
사용하여 문제를 해결할 수 있다.
"""