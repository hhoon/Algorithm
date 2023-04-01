import sys
N = int(sys.stdin.readline())
sett = set()
cnt = 0

for i in range(N) :
    a = input()
    if a != "ENTER" and a not in sett :
        sett.add(a)
        cnt += 1
    elif a == "ENTER" :
        sett.clear()
print(cnt)

"""
해당 문제를 풀기위해 set의 clear함수를 사용하였다.
clear함수를 사용해서 set을 지워줄 수 있었다.
그래서 ENTER가 아니고 set에 값이 없을 경우는 set에 해당 값을 넣어주고
cnt를 증가시켜주었다.
ENTER일 경우는 set을 초기화 시켜주므로써 문제를 해결할 수 있었다.

문제를 많이 풀어봄으로써 생각하는 힘을 길러야겠다.
"""