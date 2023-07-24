def cantor(N, S) :
    a,b,c = S[:N//3], S[N//3:(N*2)//3], S[(N*2)//3:]

    if N == 3 :
        return f"{a} {c}"
    else :
        return f"{cantor(N // 3, a)}{' ' * (N // 3)}{cantor(N // 3, c)}"

while True :
    try :
        N = int(input())
        S = '-'*(3**N)
        if N == 0 :
            print("-")
        else :
            print(cantor(len(S), S))
    except :
        break

"""
f-string 포맷이란
print(2023년 1월)
print(2023년 2월) 이라고 할때
month = 1
print (f"2023년{month}월") 과 같이 표현해서 월만 변경할 수 있다.
f 스트링을 이용하였고 처음에는 len(S)였지만 이것을 계속해서 3으로 나눠 주는 것을 a와 c를 반복하고 b의 경우는 계속 공백을 넣어주고
N==3 이 될때 이를 return 하는 방식으로 문제를 해결할 수 있다.
"""