n=input()
print(n)
print(1)

"""
해당문제를 파이썬으로 표현하면 아래와 같다.
def MenOfPassion(A, n):
    answer = 0
    for i in range(n):
        answer = answer + A[i]
    return answer

반복문을 수행하면 되서 수행횟수는 n이다.
수행시간이 상수시간에 비례하면 O
n에 비례하면 1
n2에 비례하면 2
n3에 비례하면 3
n3보다 큰 시간에 비례하면 4 라고 한다.
그래서 1이다.
"""