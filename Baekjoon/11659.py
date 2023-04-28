import sys
N, M = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))
for i in range(N-1) :
    li[i+1] += li[i]
li = [0] + li

for k in range(M) :
    i, j = map(int, sys.stdin.readline().split())
    print(li[j] - li[i-1])

"""
처음 문제를 풀었을때는 구간별 합계를 구하니 이중for문의 형태를 띄었고
이중 for문이므로 시간이 오래걸려 시간초과가 발생하였다.

그래서 아래와 같은 식으로 먼저 누적합을 구해주었다.
for i in range(N-1) :
    li[i+1] += li[i]
ex) 5 4 3 2 1 일경우
li[1] = li[1] (4)   + li[0] (5)
li[1] = 9
li[2] = li[2] (3)   + li[1] (9)
li[2] = 12
li[3] = li[3] (2)   + li[2] (12)
li[3] = 14
li[4] = li[4] (1)   + li[3] (14)
li[4] = 15
li = [5, 9 ,12, 14, 15]가 된다.
그리고 li의 맨 앞에 0을 추가해주므로써 인덱스 초과가 일어나지 않게 해줄 수 있다.
이후 i, j가 1, 3이라고 한다면
12 - 0이 되므로 5 + 4 + 3을 더한 답 12와 같게 된다.
만약 i, j가 2, 4라고 한다면
14 - 5가 되므로 4 + 3 + 2를 더한 답 9와 같게 된다.
"""