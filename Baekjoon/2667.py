"""
1. 아이디어
2중 for문
값이 1이고 방문 안한곳
DFS

2. 시간복잡도
V + E
N^2 + 4N^2 = 5N^2
= 625

3. 자료구조
그래프 저장 int[][]
방문여부 bool[][]
결과값 int[]
"""

def dfs(y, x) :
    global cnt
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]

    for k in range(4) :
        ny = dy[k] + y
        nx = dx[k] + x
        if 0 <= ny < N and 0 <= nx < N :
            if house[ny][nx] == 1 and visit[ny][nx] == False :
                visit[ny][nx] = True
                cnt += 1
                dfs(ny,nx)

N = int(input())
house = [list(map(int, input())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
answer = []
for j in range(N) :
    for i in range(N) :
        if house[j][i] == 1 and visit[j][i] == False :
            cnt = 1
            visit[j][i] = True
            dfs(j, i)
            answer.append(cnt)

answer.sort()
print(len(answer))
for i in range(len(answer)) :
    print(answer[i])

"""
ny, nx 부분을 아래와 같이 해주어서 y와 x의 값이 계속 변해 틀린 답이 나왔다.
새로운 변수에 넣어주자.
y = dy[k] + y
x = dx[k] + x

ny = dy[k] + y
nx = dx[k] + x

DFS문제를 많이 풀어보도록 하자.
"""