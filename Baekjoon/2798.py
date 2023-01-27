import itertools

N, M = map(int,input().split())
li = list(map(int,(input().split())))
select = list(itertools.combinations(li, 3))
sum = 0
selectlist = []

for i in select :
    sum = i[0] + i[1] + i[2]
    if sum <= M :
        selectlist.append(int(sum))
print(max(selectlist))

"""
해당문제는 3중 for문을 사용하여 모두 다 더해봐서 푸는 방법 있고
itertools에 있는 combinations함수를 사용하는 방법 있다.
combination 함수를 사용하면 for문을 사용하지 않고도 원하는 경우의 수를
모두 구할 수 있다.
itertools.combinations(객체, 개수)로 사용할 수 있으며
앞에 list(itertools.combinations(객체, 개수))처럼 list와 같이 알맞게
입력해줘야 한다.
"""