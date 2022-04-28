N = int(input())
a = list(input())
b = []
sum = 0

for i in range(N) :
    b.append(int(a[i]))

for j in range(len(b)) :
    sum += b[j]

print(sum)