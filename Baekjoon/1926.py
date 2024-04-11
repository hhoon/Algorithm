"""
2중 for문, 개수+1, BFS 사용, BFS 돌면서 최대값 갱신

시간복잡도 O(V+E)
V = M * N
E = 4V
5V = 5 * 500 * 500
= 1250000 < 2억개

2차원 배열, queue 사용, 방문여부(bool)
"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(y,x) :
    q = deque()
    q.append((y,x))
    rs = 1

    while q :
        ey, ex = q.popleft()
        for k in range(4) :
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m :
                if paper[ny][nx] == 1 and check[ny][nx] == False :
                    check[ny][nx] = True
                    rs += 1
                    q.append((ny,nx))
    return rs

paint = 0
maxx = 0
for i in range(n) :
    for j in range(m) :
        if paper[i][j] == 1 and check[i][j] == False :
            check[i][j] = True
            paint += 1
            maxx = max(maxx, bfs(i,j))

print(paint)
print(maxx)

"""
2차원 배열이기 때문에 [i][j]일때
i가 y이고 j가 x이다.

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]는
상하좌우로 움직이는 개념으로 생각하면 된다.

* 장고 유튜브 bfs문제 참고
"""