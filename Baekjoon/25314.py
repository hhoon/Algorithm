N = int(input())
N = N // 4

for i in range(N) :
    print("long", end = " ")
    if i == N-1 :
        print("int")