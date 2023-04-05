import sys

N = int(sys.stdin.readline())
li = []

for i in range(N) :
    X = sys.stdin.readline().split()
    if "push" in X :
        li.append(int(X[1]))
    elif X[0] == "pop" :
        try :
            print(li.pop())
        except :
            print(-1)
    elif X[0] == "size" :
        print(len(li))
    elif X[0] == "empty" :
        if len(li) > 0 :
            print(0)
        else :
            print(1)
    elif X[0] == "top" :
        try :
            print(li[-1])
        except :
            print(-1)

"""
X = input().split()로 표현할때
'push 3' 과 같이 입력할 수 있는데 이럴경우 3을 표현하는 방법은 X[1]이다.
허나 'top' 과 같이 입력할 경우 top이란 값은 X가 아니라 X[0]의 값을 의미한다.
"""