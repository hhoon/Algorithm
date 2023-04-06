li = []

for i in range(3) :
    li.append(int(input()))

if sum(li) == 180 and len(set(li)) == 1 :
    print("Equilateral")
elif sum(li) == 180 and len(set(li)) == 2 :
    print("Isosceles")
elif sum(li) == 180 and len(set(li)) == 3 :
    print("Scalene")
else :
    print("Error")