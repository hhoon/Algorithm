def solution(strings, n):
    answer = []
    
    strings.sort()
    answer = sorted(strings, key = lambda x: x[n])
    return answer

"""
해당 문제를 풀때는 lambda를 이용하면 쉽게 해결할 수 있다.
lambda를 이용하는 습관을 가지자.
"""