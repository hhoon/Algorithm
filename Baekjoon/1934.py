import math
T = int(input())

for i in range(T) :
    A, B = map(int, input().split())
    print((A*B)//math.gcd(A,B))


"""
처음 for문을 사용하여 최소공배수를 구하려고 했더니 시간초과가 발생하였다.
그래서 식을 찾아보니 (A*B) // 최대공약수를 하면 최소 공배수를 구할 수
있다고 한다.
최대공약수는 math라이브러리의 gcd()를 사용하여 구할 수 있다.
최소공배수도 math라이브러리의 lcm()을 통해 구할 수 있다고 하나 파이썬
최신버젼에서 사용이 가능하다고 한다.
"""