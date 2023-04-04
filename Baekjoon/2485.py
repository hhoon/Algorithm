import math

N = int(input())
sett = set()
li = []
between = []

for i in range(N) :
    sett.add(int(input()))

li = list(sett)
li.sort()

for i in range(N) :
    if li[i] == li[-1] :
        break
    between.append(li[i+1]-li[i])

a = between[0]
for i in range(1, len(between)) :
    a = math.gcd(a, between[i])

tree_add = 0
for j in between :
    tree_add += (j // a) - 1
print(tree_add)

"""
처음 입력받은 수를 이용하여 between에 각 간격을 구해줬다.
문제에서 원하는 간격을 구하기 위해서는 간격들의 최대공약수를 구해야한다고 한다.
최대공약수를 구한 후 각 간격들에 몇개의 나무가 들어가야 하는지를 구한 후
간격들마다 중복되는 나무 1개를 빼주었다.

예를들어 2, 6, 12, 18에 나무가 심어져있으면
이 간격은 4, 6, 6이 된다.
그리고 최대공약수는 2가 된다.
그리고 나무들 간격마다 최대공약수로 나누어주면 간격마다 몇개의 나무가 필요한지
구할 수 있다. 하지만 거기서 마지막 중복되는 나무 1개는 빼줘야한다.
첫번째 간격 4에서는 2가 나오지만 -1을 해주어서 1개가 나온다.
두번째 간격 6에서는 3이 나오지만 -1을 해주어서 2개가 나오고
세번째 간격 6에서도 3이 나오지만 -1을 해주어서 2개가 나온다.
이 개수를 tree_add += 을 통해 계속해서 더해줌으로써 답을 구할 수 있다.
"""