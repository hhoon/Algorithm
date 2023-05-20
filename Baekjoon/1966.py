import sys
from collections import deque

T = int(input())
for i in range(T) :
    N, M = map(int, sys.stdin.readline().split())
    li = deque(list(map(int, sys.stdin.readline().split())))
    locate = deque([i for i in range(N)])
    cnt = 0
    if len(li) == 1 :
        print(1)
    else :
        while True :
            if max(li) != li[0] :
                li.append(li.popleft())
                locate.append(locate.popleft())
            else :
                li.popleft()
                check = locate.popleft()
                cnt += 1
                if M == check :
                    print(cnt)
                    break

"""
해당문제를 풀때 중요도가 중복이 되기 때문에 M(알고싶은 위치)의 위치를 저장하는 방법이 필요했다.
그래서 locate라는 리스트를 한개 더 만들어주어 위치를 저장할 수 있었고 해당방법을 통해
문제를 해결할 수 있었다.
"""