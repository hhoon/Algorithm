N = int(input())
li = list(map(int, input().split()))
tmp = []
target = 1

while li :
    if li[0] == target :
        li.pop(0)
        target += 1
    else :
        tmp.append(li.pop(0))

    while tmp :
        if tmp[-1] == target :
            tmp.pop()
            target += 1
        else :
            break

if not tmp :
    print("Nice")
else :
    print("Sad")

"""
while문을 실행하는 방법에 li or tmp에 값이 있을때 실행하게 하면 해당 문제처럼 문제를 풀 수 있다.
평상시에는 True를 많이 사용하는데 그러면 무조건 while문이 실행되어야 한다.
하지만 li나 tmp에 값이 없을경우 if문에서 오류가 나는데 li or tmp에 값이 있을때 while문을 실행하게 하면 이를 해결 할 수 있다.

if not li : 처음에는 이렇게 표현했는데
while li가 실행되지 않을 경우도 있기 때문에 계속 틀렸다고 나왔다.
그래서 if not tmp를 하여 해당 문제를 해결 할 수 있었다.
"""