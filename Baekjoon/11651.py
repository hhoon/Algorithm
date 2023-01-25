N = int(input())
li = []
for i in range(N) :
    x, y = map(int, input().split())
    li.append([y, x])

li.sort()
for j in range(N) :
    print(li[j][1], li[j][0])

"""
x, y의 위치를 바꾸어서 sort를 사용하는 방법도 있었다.
다음에는 문제가 잘 해결되지 않는 경우 위와 같이 함수를 사용하도록 해보자
"""