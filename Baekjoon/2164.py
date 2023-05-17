import sys
from collections import deque
N = int(input())

li = deque([i for i in range(N, 0, -1)])
while True :
    if len(li) == 1 :
        break
    li.pop()
    a = li.pop()
    li.appendleft(a)
print(li[0])