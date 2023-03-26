N = int(input())
li_x = []
li_y = []
for i in range(N) :
    x, y = map(int, input().split())
    li_x.append(x)
    li_y.append(y)
    
x = max(li_x) - min(li_x)
y = max(li_y) - min(li_y)
print(x*y)