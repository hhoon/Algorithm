def fib(n) :
    a,b = 1,1
    for i in range(n-2) :
        a, b = b, a+b
    return b
    
def fibonacci(n) :
    f = [0] * 41
    f[1], f[2] = 1, 1
    result = 1

    for i in range(3, n) :
        f[i] = f[i-1] + f[i-2]
        result += 1

    return result
n = int(input())
print(fib(n), fibonacci(n))

"""
해당문제를 문제에서 알려준대로 파이썬으로 풀 경우 재귀함수로 구현된 fib는
시간초과가 발생한다.
그래서 그리디한 방법(Greedy Algorithm)으로 풀면 위와 같이 나타낼 수 있다고
한다.
그리고 fibonacci의 경우 해당문제에 나와 있는 식을 파이썬으로 표현하면
위와 같이 표현할 수 있다고 한다.
해당문제는 두 방법을 사용했을때 얼마나 차이가 나는지를 확인하려고 하는 문제다.
"""