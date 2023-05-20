import sys
from collections import deque
N = int(sys.stdin.readline())
li = deque()
for i in range(N) :
    inputt = sys.stdin.readline().split()
    if inputt[0] == "push_front" :
        li.appendleft(inputt[1])
    elif inputt[0] == "push_back" :
        li.append(inputt[1])
    elif inputt[0] == "pop_front" :
        try :
            print(li.popleft())
        except :
            print(-1)
    elif inputt[0] == "pop_back" :
        try :
            print(li.pop())
        except :
            print(-1)
    elif inputt[0] == "size" :
        print(len(li))
    elif inputt[0] == "empty" :
        if len(li) == 0 :
            print(1)
        else :
            print(0)
    elif inputt[0] == "front" :
        try :
            print(li[0])
        except :
            print(-1)
    elif inputt[0] == "back" :
        try :
            print(li[-1])
        except :
            print(-1)