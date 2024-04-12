from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [0] * (N+1)

def bfs(N, M, R) :
    q = deque([R])
    cnt = 1
    visit[R] = cnt

    while q :
        n = q.popleft()
        
        for i in graph[n] :
            if visit[i] == 0 :
                cnt += 1
                visit[i] = cnt
                q.append(i)

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in range(N+1) :
    graph[j].sort()

bfs(N, M, R)

for i in range(1, len(visit)) :
    print(visit[i])

"""
graph[u].append(v)는 graph의 '1번 위치'에 1번과 연결되어 있는 얘들을 넣어주는것이다.
그리고 양 방향이기때문에 graph[v].append(u)도 해주어야한다.

그리고 오름차순이기때문에 graph[j].sort()를 해준다.
(ex 1번에 연결되어 있는 것들중 오름차순으로 정렬한다. 2, 3, 4 ...

n = q.popleft()
여기서 n은 정점의 위치이다.
for i in graph[n] 시작이 R=1 이기때문에 1번과 연결된것들부터 q에 넣어주고 q.popleft()를 통해 다음 graph[n]을 확인해준다.
visit에 방문한 순서대로 cnt를 넣어준다.

아직 알고리즘을 이해하는데 시간이 많이 걸리고 있다. 문제를 많이 풀어봐서 알고리즘을 조금 더 빨리 파악해야겠다.
"""