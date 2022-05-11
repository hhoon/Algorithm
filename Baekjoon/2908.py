A, B = input().split()
s = []
s.append(A)
s.append(B)
reverse = []

for i in range(len(s)) :
    for j in range(2,-1,-1) :
        reverse.append(s[i][j])

a = int(reverse[0]+reverse[1]+reverse[2])
b = int(reverse[3]+reverse[4]+reverse[5])

if a > b :
    print(a)
elif a < b :
    print(b)

"""
문제의 조건에 맞게 잘 출력 했는지 확인하기
"""