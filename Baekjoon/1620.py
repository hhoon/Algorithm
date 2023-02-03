import sys
N, M = map(int, sys.stdin.readline().split())
dic = {}

for i in range(1, N+1) :
    inputt = sys.stdin.readline().rstrip()
    dic[str(i)] = inputt
    dic[inputt] = i

for j in range(M) :
    check = sys.stdin.readline().rstrip()
    print(dic[check])

"""
처음 리스트를 사용하여 문제를 풀었는데 계속 시간초과가 발생하였다.
딕셔너리를 사용하여 풀려고 했는데 (키 : 값) 중 값은 구할 수 있었지만
키 값을 출력할 수 없어 해당 키를 값으로 한번 더 넣어주었다.
이후에도 시간초과가 계속 발생하여서 보니 sys.stdien.readline()을
사용하였고 이후에는 오류가나서 ex) 25\n 이런식으로 오류가 나서 rstrip()
함수를 사용하여 문제를 해결할 수 있었다.
"""