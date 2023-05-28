n = int(input())
li = list(map(int, input().split()))

for i in range(1, n) :
    li[i] = max(li[i], (li[i-1] + li[i]))
print(max(li))

"""
해당문제는 이전까지 모든 숫자의 합 중 최대값을 그때 그때 기록 하는 것이다.
반복문을 1부터 시작하는 이유는 데이터의 시작점인 0번 인덱스는 이전까지의 합이
0번 인덱스이기 때문에 1부터 시작한다.

li[i] = max(li[i], (li[i-1] + li[i]))
10 -4 3 1 5 6 -35 12 21 -1 이라고 할때,
li[1] = max(-4, 6) = 6
li[2] = max(3, 9) = 9
li[3] = max(1, 10) = 10

위와 같이 max를 사용하기때문에 이전까지의 합이 크면 계속 누적이되고
작다면 현재 자신의 값이 max가 된다.

li[4] = max(5, 15) = 15
li[5] = max(6, 21) = 21
li[6] = max(-35, -14) = -14
li[7] = max(12, -2) = 12
li[8] = max(21, 33) = 33
li[9] = max(-1, 32) = 32

위와 같이 나타낸후 max(li)를 통해 최대값을 구할 수 있다.
"""