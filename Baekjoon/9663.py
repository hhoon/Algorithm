import sys

N = int(sys.stdin.readline())
answer = 0
v1 = [0] * N            # 행
v2 = [0] * (2*N-1)      # 대각선
v3 = [0] * (2*N-1)      # 반대쪽 대각선

def dfs(i) :
    global answer
    if i == N :
        answer += 1
        return
    
    for j in range(N) :
        if v1[j] or v2[i+j] or v3[i-j] :
            continue
        v1[j], v2[i+j], v3[i-j] = 1, 1, 1
        dfs(i+1)
        v1[j], v2[i+j], v3[i-j] = 0, 0, 0

dfs(0)
print(answer)

"""
예를 들어 4x4 (ixj) 는 아래와 같다.
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
(3,0) (3,1) (3,2) (3,3)

아래와 같은 경우 말을 놓는 위치가 겹친다.
직선 = j
대각선(/) = 합이 같다는 공통점 이용 (i+j)
대각선(\) = 차이가 같음 (i-j)
v1 = 열
v2 = 대각선
v3 = 반대쪽 대각선
v1[j] == v2[i+j] == v3[i-j] == 0 이라면 말을 놓을 수 있다.
하지만 if v1[j] or v2[i+j] or v3[i-j] 와 같이 하나라도 1(True) 이라면 말을 놓을 수 없고 다음 for문의 j값을 실행한다.
v1[j] == v2[i+j] == v3[i-j] == 0 이라면 놓은 후 1이라고 표시해주기
1이라고 표시를 해주고도 i행부터 체크해서 N까지 갔다면 한개의 경우의 수가 가능하기 때문에 answer += 1 해주기
answer += 1을 해주고 v1[j], v2[i+j], v3[i-j] = 0, 0, 0을로 초기화 해주고
j에 1을 더해 다음 for문을 실행하는 식으로 반복함으로써 답을 구할 수 있다.

DFS(깊이우선탐색) 및 Backtracking(백트레킹)을 조금 더 공부해 봐야겠다.
"""