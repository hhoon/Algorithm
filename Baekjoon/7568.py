N = int(input())
li = []
compare = []
for i in range(N) :
    li.append(list(map(int, input().split())))

for i in li :
    rank = 1
    for j in li :
        if i[0] < j[0] :
            if i[1] < j[1]:
                rank += 1
    compare.append(int(rank))
for i in compare :
    print(i, end =' ')

"""
처음에는 i[0] > j[0] 이고 i[1] > j[1] 일때 cnt += 1 로 해서 구해보니
[1, 1, 4, 1, 0]으로 자신이 해당 리스트에서 몇명보다 큰지를 표현하였고
그 상태에서 등수를 구하려니 고생을 했다.
하지만 반대로 i[0] < j[0] 이고 i[1] < j[1] 일때 등수를 1씩 더해보니
가장 해당 리스트의 등수를 구할 수 있었다.
문제를 풀때 해결이 되지 않으면 다른 방법으로 접근해 보도록 해야겠다.
"""