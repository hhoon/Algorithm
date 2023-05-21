import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
select = deque()
select.append(list(map(int, sys.stdin.readline().split())))
li = deque([ i for i in range(1, N+1)])
num = 0
cnt = 0

while len(li) != (N-M) :
    if select[0][num] == li[0] :
        li.popleft()
        num += 1
    elif (len(li)/2) < li.index(select[0][num]) :
        li.appendleft(li.pop())
        cnt += 1
    elif (len(li)/2) >= li.index(select[0][num]) :
        li.append(li.popleft())
        cnt += 1
print(cnt)

"""
해당문제를 풀때는 최솟값을 구해야한다.
그래서 제거해야하는 원소의 인덱스 값을 찾아주고 그 값의 중간을 찾아서
가까운 곳을 구한 후 왼쪽으로 이동할지 오른쪽으로 이동할지를 위와 같이
구했다.
위와 같은 방법으로 문제를 해결할 수 있었다.
"""