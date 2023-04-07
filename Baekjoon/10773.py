import sys

N = int(sys.stdin.readline())
li = []

for i in range(N) :
    money = int(sys.stdin.readline())
    if money == 0 :
        li.pop()
    else :
        li.append(money)
print(sum(li))