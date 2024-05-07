import sys
sys.setrecursionlimit(10**6)

"""
1. 아이디어
for문 사용
dfs 사용
2. 시간복잡도
dfs (V+E)
100000 + 200000 = 300000

3. 자료구조
graph = []
visit = []
result = []
"""

def dfs(R) :
    global cnt

    if visit[R] == 0 :
        cnt += 1
        visit[R] = cnt
        
        for i in graph[R] :
            dfs(i)
    
N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visit = list(0 for _ in range(N+1))
cnt = 0

for i in range(M) :
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for j in range(len(graph)) :
    graph[j].sort(reverse=True)

dfs(R)

for k in range(1, len(visit)) :
    print(visit[k])

"""
24479와 같은 방식으로 문제를 풀었는데도 계속해서 시간초과가 나왔다.
코드를 자세히 보니 중간에 sys.stdin.readline()을 안쓰고 input()을 사용하여 시간초과가 발생했다.
앞으로 해당부분에 유의하며 문제를 풀자
"""