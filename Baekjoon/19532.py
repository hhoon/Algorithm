import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
brk = 0
for x in range(-999, 1000) :
    for y in range(-999, 1000) :
        if (a*x + b*y == c) and (d*x + e*y == f) :
            print(x, y)
            brk = 1
            break
    if brk == 1 :
        break

"""
처음 해당문제를 풀기 위해 아래와 같이 식을 세워서 풀었더니 런타임 에러가
발생하였다.
a, b, c, d, e, f = map(int, input().split())

x = ((e*c) -(b*f)) / ((a*e)-(b*d))
y = (c - (a*x)) / b
print(int(x), int(y))

찾아보던중 수학식으로 푸는방법도 있지만 for문을 사용하여 위와 같이 모두
넣어봐서 x와 y를 구하는 방법이 있었다.
그런데 계속 시간초과가 발생하여 break도 넣어보고 sys.stdin.readline()도
사용해보았지만 시간초과를 해결할 수 없었다.
그러던중 기존에 작성한 코드인
if (a*x + b*y == c) & (d*x + e*y == f) : 에서
&를 and로 바꿔주니 시간초과를 해결 할 수 있었다.

and는 논리연산자로 두개의 조건식이 같으면 True를 리턴한다고 한다.
&의 경우는 비트연산자라고한다.
앞으로 if문을 사용할때는 and를 사용하면 조금 더 속도를 높일 수 있을것 같다.
"""