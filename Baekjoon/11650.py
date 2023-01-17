N = int(input())
li = []
for i in range(N) :
    li.append(list(map(int, input().split())))

li.sort()

for j in range(N) :
    print(li[j][0], li[j][1])

"""
li.append(list(map(int, input().split())))
list에 append로 map함수 사용시에는 map을 list로 감싸야한다.
그렇지 않으면 오류가 발생한다.
"""