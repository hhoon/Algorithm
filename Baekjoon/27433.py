def factorial(N) :
    if N == 0 :
        return 1
    answer = N * factorial(N-1)
    return answer

N = int(input())
print(factorial(N))