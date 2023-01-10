li = []
sum = 0

for i in range(5) :
    li.append(int(input()))
    sum += li[i]

li.sort()
print(int(sum/5))
print(li[2])