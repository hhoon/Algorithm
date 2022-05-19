A,B,C = map(int,input().split())
N = 0

if B >= C :
    print(-1)
else :
    N = (A // (C-B)) + 1
    print(N)

"""
while True :
        if A + (B * N) < C * N :
                print(N)
                break
        elif B >= C :
                print(-1)
                break
        else :
                N += 1
while문을 사용할경우 수를 엄청 큰수를 넣을 경우 시간이 너무 오래걸리므로
수식으로 코딩을 한다.
B >= C 처럼 수학적으로 문제에 접근해야 한다.
위의 문제를 식으로 나타내면 A + (B * N) = C * N 라고 한다.
A = (C * N) - (B *N)
A = N(C-B)
A / (C-B) = N
여기서 손익분기점을 넘기려면 해당 식에서 +1을 해줘야 이익이 생긴다.
"""