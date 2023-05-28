T = int(input())
li = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + ([0] * 90)

for i in range(T) :
    N = int(input())
    for i in range(11, N+1) :
        li[i] = li[i-1] + li[i-5]
    print(li[N])

    """
    규칙을 찾는 연습을 하도록 하자
    """