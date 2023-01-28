N = int(input())
li = []
for i in range(N) :
    age, name = input().split()
    age = int(age)
    li.append([age, name])

li.sort(key=lambda x : x[0])

for i in range(N) :
    print(li[i][0], li[i][1])

"""
lambda를 이용하여 원하는 특정요소를 기준으로 정렬할 수 있다.
age를 int형으로 바꿔주지 않으면 str형으로 2자리 수의 경우 제대로 정렬이
이루어지지 않는다.
추가로 정렬에는 stable 정렬과 unstable 정렬방식이 있다고 한다.
stable 정렬은 말 그대로 안정 정렬이다. 안정 정렬에서는 입력 받은 값들 중에
같은 값이 있는 경우 해당 값의 순서를 그대로 유지한다.
예를 들어, [1, 2, 3(X), 4, 5, 3(Y)] 을 오름차순 정렬한다면,
[1, 2, 3(X), 3(Y), 4, 5]순으로 세 번째 위치한 3의 위치와 여섯 번째
위치한 3의 위치가 바뀌지 않는다.
unstable 정렬에서는 이러한 정렬을 장담할 수 없다.
파이썬은 기본적으로 stable 정렬을 한다고 한다.
"""