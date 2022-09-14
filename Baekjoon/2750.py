n = int(input())
li = []

for i in range(n) :
    li.append(int(input()))

li.sort()

for j in range(n) :
    print(li[j])