def factorial(N) :
    multiply = 1
    if N > 0 :
        multiply = N * factorial(N-1)
    return multiply

N = int(input())
print(factorial(N))


"""
재귀함수의 개념에 대해 다시 한번 익히고 함수 사용법 공부하기
"""