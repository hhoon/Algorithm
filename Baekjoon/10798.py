li = []
len_li = []
for i in range(5) :
    li.append(input())

for i in li :
    len_li.append(len(i))

for i in range(max(len_li)) :
    for j in range(5) :
        try :
            print(li[j][i], end='')
        except :
            continue