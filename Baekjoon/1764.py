import sys

N, M = map(int, sys.stdin.readline().split())
listen = []
see = []
answer = []
for i in range(N) :
    listen.append(sys.stdin.readline().rstrip())
for i in range(M) :
    see.append(sys.stdin.readline().rstrip())
listen = set(listen)
see = set(see)
for i in see :
    if i in listen :
        answer.append(i)
answer.sort()

print(len(answer))
for i in answer :
    print(i)

"""
문제를 풀었을때 출력은 잘 되는데 계속 틀려서 원인을 찾아봤더니 사전 순서대로
출력하라는 말이 있었다.
문제를 풀을 때 놓치는 부분이 없도록 꼼꼼히 읽어보고 풀도록 하자.
"""