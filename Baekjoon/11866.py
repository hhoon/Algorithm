import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
li = deque([i for i in range(1, N+1)])
yfs = []

while len(li) > 0 :
    for i in range(K-1) :
        li.append(li.popleft())
    yfs.append(li.popleft())
    
print("<", end = "")
for i in yfs :
    if i == yfs[-1] :
        print(str(i), end = "")
    else :
        print(i, end = "")
        print(",", end = " ")
print(">")

"""
해당문제를 풀는 방법은 k의 앞은 모두 뒤로 넘겨주는 방식으로 해결 할 수 있다.
그리고 append에 popleft()값을 넘어주기만해도 자동으로 popleft()가 되는
것을 알 수 있다.
"""