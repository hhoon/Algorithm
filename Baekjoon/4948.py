import sys

li = []
for i in range(1, 123456*2+1) :
    check = 0
    for j in range(2, int(i**0.5)+1) :
        if i % j == 0 :
            check = 1
            break
    if check == 0 :
        li.append(i)

while True :
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    elif n == 1 :
        print(1)
    else :
        count = 0
        for i in li :
            if n < i <= (2*n) :
                count += 1
        print(count)

"""
해당 문제를 풀때 계속해서 시간 초과가 발생하였다.
처음에는 아래와 같이 코드를 작성하였었다.

import sys

while True :
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    elif n == 1 :
        print(1)
    else :
        count = 0
        for i in range(n+1, (2*n)+1) :
            count += 1
            for j in range(2, int(i**(1/2))+1) :
                if i % j == 0 :
                    count -= 1
                    break
        print(count)
하지만 계속해서 시간초과가 발생하여 해당문제의 제한 범위인 123456까지
미리 소수를 구해준 후 그 소수들의 범위 안에서 문제를 풀으니 속도가 많이
빨라져 문제를 해결할 수 있었다.
"""