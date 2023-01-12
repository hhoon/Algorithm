import sys, math
from collections import Counter
N = int(sys.stdin.readline())
li = []
sum = 0

for i in range(N) :
    li.append(int(sys.stdin.readline()))
    sum += li[i]

li.sort()

print(round(sum/N))   # 산술평균
print(li[math.floor(N/2)])   # 중앙값

mostt = Counter(li).most_common()
if len(mostt) > 1 :   # 최빈값
    if mostt[0][1] == mostt[1][1] :
        print(mostt[1][0])
    else :
        print(mostt[0][0])
else :
    print(mostt[0][0])

print(max(li)-min(li))   # 범위:

"""
해당 문제를 풀기 위해서는 반올림(round), 올림(ceil), 내림(floor) 등의 함수를 사용 및 collections 모듈에서 Counter함수를 사용하여
문제를 풀 수 있었다. 꾸준히 공부해서 여러 함수들의 사용법을 익혀야겠다.
"""