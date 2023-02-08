import sys

N = int(sys.stdin.readline())
Nlist = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
Mlist = list(map(int, sys.stdin.readline().split()))

cnt = {}
for i in Nlist :
    if i in cnt :
        cnt[i] += 1
    else :
        cnt[i] = 1

for i in Mlist :
    if i in cnt :
        print(cnt[i], end =' ')
    else :
        print(0, end = ' ')

"""
count함수를 사용하여 처음에 풀었더니 시간초과가 발생하였다.
그래서 dictionary를 사용해서 풀어야는데 위와 같이 dictionary를 사용하면
count의 기능을 할 수도 있다. dictionary의 다양한 사용법을 익히도록 하자.
"""