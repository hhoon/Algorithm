import sys

N, M = map(int, sys.stdin.readline().split())
dic = {}
for i in range(N) :
    inputt = sys.stdin.readline().strip()
    if len(inputt) >= M :
        if inputt in dic :
            dic[inputt] += 1
        else :
            dic[inputt] = 1

dictionary = sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for i in dictionary :
    print(i[0])

"""
sort(key=lambda x :(기준1, 기준2, 기준3))이라 한다.
여러개의 기준이 나오면 앞에있는 기준부터 차례대로 정렬하고 동일 값이
나오면 그 다음 기준으로 정렬을 한다.

sort(key = lamba x : (기준), reverse = True)를 해주면 내림차순이 가능하다.
단, 모든 기준들이 일괄적으로 내림차순이 된다고 한다.

기준마다 각각 오름차순, 내림차순을 다르게 설정해줄 때는 기준 앞에 -를 붙여
설정해줄 수 있다고 한다.
다만 이는 숫자형만 적영 되는 것이고 문자형은 적용이 되지 않는다고 한다.

inputt을 통해
('sand', 3)
('apple', 2)
('append', 1) 와 같은 형태로 저장해 주었다.

그러므로
dictionary = sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
-x[1]은 3,2,1과 같은 숫자를 내림차순으로 정렬한것이고, x[0] = sand, apple과
같은 단어의 길이를 내림차순으로 정렬한 것이고, x[0]은 단어 그대로를 오름차순
으로 정렬한 것이다.
그리고 key, value 쌍을 얻기 위해 items()를 사용하였다.
"""