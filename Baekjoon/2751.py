import sys

N = int(input())
group = []

for i in range(N) :
    a = int(sys.stdin.readline())
    group.append(a)

group.sort()

for j in range(N) :
    print(group[j])


"""
수가 방대할 경우 input을 사용하면 입력되는 양이 많아 시간초과가
발생하게 된다. 그래서 input() 대신 sys.stdin.readline() 함수를 사용하여
이를 해결할 수 있다.
"""