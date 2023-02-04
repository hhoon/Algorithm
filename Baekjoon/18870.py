import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
sett = set(li)
tmp = sorted(sett)
dic = {}

for i in range(len(tmp)) :
    dic[tmp[i]] = i

for i in li :
    print(dic[i], end =' ')

"""
해당문제를 풀때 문제의 뜻이 이해가 가지 않아 찾아보니
좌표 압축이란?
여러곳에 흩뿌려진 좌표들을 연속된 수들로 모아 압축하는 것이라고 한다.
ex) [1, 10, 10000, 1000000] 이렇게 네 점의 좌표가 있다고 하고
이 좌표를 압축하여 순서대로 표현한다면 [0, 1, 2, 3] 이라고 한다.

처음 문제를 풀때는 index값을 활용하여 풀이하였더니 시간초과가 발생하였다.
시간초과에 대해 찾아본 결과는 이러했다.
list.index(i)의 형태는 시간 복잡도 O(N)을 가지고 있고 매번 최대
1,000,000번의 수행이 이루어지게 되어 시간초과가 발생한다고 한다.
하지만 딕셔너리는 dic[요소] : 요소의 index의 형태로 저장함으로써
dic[i]의 형태로 시간복잡도는 O(1)이라고 한다.
정리하자면 아래와 같이 표현할 수 있다.
    list.index(i)의 시간 복잡도 = O(N)
    dic[i]의 시간복잡도 = O(1)
이러한 형태이기 때문에 해당문제는 딕셔너리를 사용하여 풀면 시간초과의
문제를 해결할 수 있다.
"""