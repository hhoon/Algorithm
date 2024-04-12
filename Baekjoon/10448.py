from itertools import product
import sys
input = sys.stdin.readline

T = int(input())
answer = [0] * T
cnt = 0
for i in range(T) :
    check = int(input())
    li = [a for a in range(1, check+1)]

    for j in range(1, len(li)) :
        li[j] = li[j] + li[j-1]
        if li[j] >= check :
            li = li[:j]
            break

    for k in product(li, repeat=3) :
        if sum(k) == check :
            answer[cnt] = 1
            break
    cnt += 1

for l in answer :
    print(l)

"""
li에 값을 미리 넣어줬기 때문에 아래의 if문을 사용하지 않으면 틀린답이 나왔다.
if li[j] >= check :
    li = li[:j]
    break
    
product를 사용하여 3개의 합을 구할 수 있었다.
"""