import sys

N = int(input())
A = set(map(int, sys.stdin.readline().split()))
M = int(input())
B = list(map(int, sys.stdin.readline().split()))

for i in range(M) :
    if B[i] in A :
        print(1)
    else :
        print(0)

"""
A를 list로 만들어 실행하면 시간초과가 발생한다.
그래서 list가 아닌 set을 활용하면 중복을 허용하지 않기 때문에 시간초과를
해결할 수 있다.
if문 사용시 B[i] in A 처럼 in (리스트나 set 등등)의 형태로도 사용이
가능하다.
"""