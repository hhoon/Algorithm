N, M = map(int, input().split())
S = []
check = []
cnt = 0
for i in range(N) :
    S.append(input())

for i in range(M) :
    check.append(input())

for i in check :
    if i in S :
        cnt += 1

print(cnt)