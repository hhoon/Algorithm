li = list(map(int, input().split()))
N = li[0]
k = li[1]
score = list(map(int, input().split()))
score.sort()
for i in range(N, 0, -1) :
    if i-1 == N-k :
        print(score[i-1])