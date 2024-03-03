def solution(s):
    answer = False
    cnt = 0
    if len(s) == 4 or len(s) == 6 :
        if s.isdecimal() :
            answer = True
    return answer

"""
문제를 풀때 문자열 s의 길이가 4 혹은 6이라는 조건을 빼먹어서 계속 틀린 답이 나왔다.
이후 if len(s) == 4 or 6 이라고 입력을 해서 계속 틀린 답이 나왔다.
길이가 4 혹은 6을 입력 할때는 위와 같이 입력하면 안되고 len(s) == 4 or len(s) == 6 이라고
입력하는것에 주의하자.
그리고 문제를 꼼꼼히 읽는 습관을 들여야겠다.
"""