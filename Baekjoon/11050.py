N, K = map(int, input().split())
A = 1
B = 1
C = 1

for i in range(K,0,-1) :
    A *= i
for i in range((N-K),0,-1) :
    B *= i
for i in range(N,0,-1) :
    C *= i
print(int(C/(A*B)))

"""
이항계수가 무엇인지 찾아보았다.

nCk로 표현되는 조합을 말한다고 적혀있다.
즉, n개 중에서 k개를 순서 없이 고르는 방법의 가짓수를 말한다.
5C2 는 5개 중에서 2개를 고르는 방법이며, 이 때 순서는 필요 없다.

두개의 바구니가 있을 때 첫번째 바구니에는 5개중 5개를 선택할 수 있으며,
두번째 바구니에는 4개 중에서 한개를 고르면 된다.
즉 5*4=20가지가 된다. 이 때는 순서를 고려해서 뽑은 것이다. 

그러면 순서 없이 뽑으려면 2개를 줄 세우는 가짓수인 2! = 2*1을 나눠주면 된다.
즉 20/2 = 10이 나온다.

이를 식으로 표현하면 아래와 같이 표현할수 있다고 한다.
( n )  =  n! / k!(n-k)!
( k )

해당식을 가지고 문제를 해결할 수 있었다.
"""