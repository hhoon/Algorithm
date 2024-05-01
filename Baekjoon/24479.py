import sys
sys.setrecursionlimit(10 ** 6)
"""
1. 아이디어
for문 사용
DFS 사용
2. 시간복잡도
V + E = 100000 + 200000
= 3000000
3. 자료구조
방문 여부를 cnt로 저장 int[]
graph int[]
"""
def dfs(R) :
    global cnt
    if visit[R] == 0 :
        visit[R] = cnt
        cnt += 1
        for i in graph[R] :
            dfs(i)

N, M, R = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visit = [0] * (N+1)
cnt = 1

for i in range(M) :
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph :
    i.sort()

dfs(R)
for i in range(1, len(visit)) :
    print(visit[i])

"""
답은 제대로 나왔으나 제출시 계속해서 런타임 에러가 발생했다.
찾아보니 dfs를 파이썬으로 풀 경우에는 반드시 sys.setrecursionlimit(10 ** 6) 를 써줘야 한다고 한다.
파이썬의 경우 재귀의 깊이 제한이 1000으로 매우 얕아서 sys.setrecursionlimit(10 ** 6)를 사용하여 재귀의 최대 깊이를 10 **6 으로 설정하여 문제를 해결할 수 있다고 한다.
"""