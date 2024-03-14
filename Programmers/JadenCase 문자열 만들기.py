def solution(s):
    answer = ''

    for i in range(len(s)) :
        if i == 0 and s[0].isalpha() == True :
            answer += s[i].upper()
        elif s[i-1] == ' ' :
            answer += s[i].upper()
        else :
            answer += s[i].lower()
    return answer

"""
문자 s의 맨 앞이나 끝이 공백일 경우의 수가 있어 s = list(map(str),s.split())으로는
풀면 오답이 나온다.
앞이 공백인 경우와 같이 다른 경우의 수도 생각하며 문제를 풀도록 하자
"""