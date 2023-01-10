N, M = input().split()
A = []
B = []

for i in range(int(N)) :
    A.append(input().split())

for j in range(int(N)) :
    B.append(input().split())

for k in range(int(N)) :
    for l in range(int(M)) :
        print(int(A[k][l])+int(B[k][l]), end =" ")
    print(end = "\n")