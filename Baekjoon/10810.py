N, M = map(int, input().split())
li = [0]*N

for a in range(M) :
    i, j, k = map(int, input().split())
    for b in range(i-1, j) :
        del li[b]
        li.insert(b, k)

for c in li :
    print(c, end=" ")

"""
리스트에서 remove()를 사용하면 해당하는 값의 첫번째 값을 지울 수 있다.
ex) [1, 2, 3, 1, 2, 3]
remove(3)
[1, 2, 1, 2, 3]

del li[i]를 입력하면 원하는 위치의 값을 지울 수 있다.
"""