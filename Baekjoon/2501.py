N, K = map(int, input().split())
li = []
try :
    for i in range(1, N+1):
        if N % i == 0 :
            li.append(i)
    li.sort()
    print(li[K-1])
except :
    print("0")