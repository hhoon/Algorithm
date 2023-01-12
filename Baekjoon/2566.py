li = []
li2 = []
tmp = []
for i in range(9) :
    li.append(input().split())
    li2.append(map(int, li[i]))
    tmp.append(max(li2[i])) 
maxx = max(tmp)

print(maxx)
brk = True
for j in range(9) :
    for k in range(9) :
        if int(li[j][k]) == maxx :
            brk = False
            print(j+1, k+1)
            break
    if brk == False :
        break

"""
break는 이중 for문에서 안쪽에 있는 for문 안에만 사용하면 안쪽에 있는
for문만 빠져 나오기때문에 바깥쪽 for문에 까지 총 2개 사용해줘야한다.
"""