S = input()
li = []

for i in range(len(S)) :
    for j in range(i, len(S)) :
        li.append(S[i:j+1])
li = set(li)
print(len(li))

"""
해당문제를 풀기 위해서는 이중 for문을 사용하여야 한다.
이중 for문을 사용하여 안쪽에 있는 for문에 시작점을 i로 주고 S[i:j+1]로
표현함으로써 처음에는 a, ab, aba, abab, ababc
두번째는 b, ba, bab, babc 이런식으로 전부다 넣어준 다음
중복된 값을 제거해서 문제를 풀 수 있었다.

문제를 많이 풀어봐서 문제를 해결하는 여러 방법들을 익혀야겠다.
"""