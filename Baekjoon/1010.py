import sys
def factorial(num) :
    fact_num = 1
    for i in range(num, 0, -1) :
        fact_num *= i
    return fact_num

T = int(sys.stdin.readline())
for i in range(T) :
    N, M = map(int, sys.stdin.readline().split())
    answer = factorial(M) // (factorial(M-N) * factorial(N))
    print(answer)

"""
해당 문제를 푸는 공식 mCn으로 해결 할 수 있다고 한다.
m이 n보다 크기 때문에 최대 연결할 수 있는 다리의 개수는 n개이고 m개의 지역에 n개의 다리를
놓을 수 있는 경우의 수를 구하는 것이기 때문에 mCn으로 표현할 수 있다고 한다.
mCn = m! // (m-n)!*n! 와 같다고 한다.

이는 예제에서
2 2 (2C2) = 1 
1 5 (5C1) = 1
13 29 (29C13) = 67863915
으로 먼저 유추할 수 있다.
"""