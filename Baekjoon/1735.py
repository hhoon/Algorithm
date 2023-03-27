import math

li_a = []
li_b = []

for i in range(2) :
    A, B = map(int, input().split())
    li_a.append(A)
    li_b.append(B)

A = li_a[0]*li_b[1] + li_a[1]*li_b[0]
B = li_b[0]*li_b[1]
C = math.gcd(A, B)

print(A // C, B // C)

"""
기약분수를 구하기 위해서는 분자와 분모를 최대공약수로 나누면 된다고 한다.
"""