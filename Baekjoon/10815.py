import sys

N = int(sys.stdin.readline())
sangguen = set(map(int,sys.stdin.readline().split()))
M  = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))
answer = []

for i in range(M) :
    if check[i] in sangguen :
        answer.append(1)
    else :
        answer.append(0)
for i in answer:
    print(i, end=' ')

"""
check.append(list(map(int,sys.stdin.readline().split())))
이런 형태로 넣게 되면 [[1, 2, 3]] 이런 형태로 들어가니 주의 하자
이 문제는 list형을 사용하면 시간초과가 발생한다. 그래서 set함수를 이용하였다.
set함수는 count()나 index()와 같이 list에서 사용하는 함수들은 사용할 수 없다.
그럼으로 if check[i] in sangguen : 와 같이 표현하면 해당 set함수 안의
요소들을 찾을 수 있다.
"""