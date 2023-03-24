import math

A, B = map(int, input().split())
answer = (A*B) // math.gcd(A,B)
print(answer)