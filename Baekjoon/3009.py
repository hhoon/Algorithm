li_a = []
li_b = []
answer = []
for i in range(3) :
    a, b = map(int, input().split())
    li_a.append(a)
    li_b.append(b)

for i in li_a :
    if li_a.count(i) == 1 :
        answer.append(i)
for i in li_b :
    if li_b.count(i) == 1 :
        answer.append(i)
print(answer[0], answer[1])