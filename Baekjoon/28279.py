from collections import deque
import sys

N = int(sys.stdin.readline())
li = deque()

for i in range(N) :
    inputt = sys.stdin.readline().split()
    
    if inputt[0] == '1' :
        li.appendleft(inputt[1])
    elif inputt[0] == '2' :
        li.append(inputt[1])
    elif inputt[0] == '3' :
        if len(li) == 0 :
            print('-1')
        else :
            print(li.popleft())
    elif inputt[0] == '4' :
        if len(li) == 0 :
            print('-1')
        else :
            print(li.pop())
    elif inputt[0] == '5' :
        print(len(li))
    elif inputt[0] == '6' :
        if len(li) == 0 :
            print('1')
        else :
            print('0')
    elif inputt[0] == '7' :
        if len(li) == 0 :
            print('-1')
        else :
            print(li[0])
    elif inputt[0] == '8' :
        if len(li) == 0 :
            print('-1')
        else :
            print(li[-1])