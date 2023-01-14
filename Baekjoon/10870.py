n = int(input())

fibonacci = [0, 1]
for i in range(n+1) :
    fibonacci.append(fibonacci[i]+fibonacci[i+1])

print(fibonacci[n])

"""
for문을 사용하는 방법뿐만 아니라 함수를 사용하여 푸는 방법도 익히자.
"""