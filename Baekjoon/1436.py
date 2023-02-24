N = int(input())
li = []
i = 0
while True :
    i += 1
    if '666' in str(i) :
        li.append(i)
    if len(li) == 10000 :
        break
li.sort()
print(li[N-1])