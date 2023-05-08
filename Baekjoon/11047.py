N, K = map(int, input().split())
li = []
cnt = 0

for i in range(N) :
    li.append(int(input()))

for i in range(len(li), 0, -1) :
    if li[i-1] <= K :
        a = K // li[i-1]
        K = K % li[i-1]
        cnt += a
    if K == 0 :
        print(cnt)
        break