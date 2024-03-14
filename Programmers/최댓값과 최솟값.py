def solution(s):
    s = list(map(int, s.split()))
    minn = min(s)
    maxx = max(s)
    answer = str(minn) + ' ' + str(maxx)
    return answer

"""
list(map)을 사용하여 s를 공백기준으로 구분할 수 있다.
공부했던거 복습하도록 하자.
"""