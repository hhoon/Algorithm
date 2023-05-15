import sys
from collections import deque
N = int(sys.stdin.readline())
li = deque()

for i in range(N) :
    a = sys.stdin.readline().split()
    if a[0] == "push" :
        li.append(int(a[1]))
    elif a[0] == "pop" :
        if len(li) > 0 :
            print(li[0])
            li.popleft()
        else :
            print(-1)
    elif a[0] == "size" :
        print(len(li))
    elif a[0] == "empty" :
        if len(li) > 0 :
            print(0)
        else :
            print(1)
    elif a[0] == "front" :
        if len(li) > 0 :
            print(li[0])
        else :
            print(-1)
    elif a[0] == "back" :
        if len(li) > 0 :
            print(li[-1])
        else :
            print(-1)