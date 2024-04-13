from collections import deque
import sys

N, M, R = map(int, sys.stdin.readline().split())
li = [[] for i in range(N+1)]
visit = [0 for j in range(N+1)]

def bfs(N, M, R) :
    q = deque([R])
    cnt = 1
    visit[R] = cnt

    while q :
        n = q.popleft()
        for i in li[n] :
            if visit[i] == 0 :
                cnt += 1
                visit[i] = cnt
                q.append(i)


for i in range(M) :
    u, v = map(int, sys.stdin.readline().split())
    li[u].append(v)
    li[v].append(u)

for j in range(N+1) :
    li[j].sort(reverse=True)

bfs(N, M, R)

for i in range(1, len(visit)) :
    print(visit[i])