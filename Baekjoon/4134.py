import sys

N = int(sys.stdin.readline())

for i in range(N) :
    number = int(sys.stdin.readline())
    while True :
        check = 0
        if number == 0 or number == 1 :
            print(2)
            break
        for j in range(2, int(number**(1/2))+1) :
            if number % j == 0 :
                check = 1
                break
        if check == 0 :
            print(number)
            break
        else :
            number += 1

"""
처음 문제를 풀때 number**(1/2)입력시 괄호를 입력안하고 number**1/2로 표현을
해서 시간초과가 발생하였다. 괄호 입력에 유의하자.
그리고 number가 0과 1일 경우를 계산을 안해서 틀린 답이 나왔었다.
이러한점이 누락되지 않게 주의하며 문제를 풀자.
"""