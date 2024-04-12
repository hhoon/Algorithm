import sys
input = sys.stdin.readline

T = int(input())
n = []
for _ in range(T) :
    n.append(int(input()))

a = [0] * (max(n)+1)
a[1] = 1
a[2] = 2
a[3] = 4

for i in range(4,max(n)+1) :
    a[i] = a[i-3] + a[i-2] + a[i-1]

for j in range(T) :
    b = n[j]
    print(a[b])