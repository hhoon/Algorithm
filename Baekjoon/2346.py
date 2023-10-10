import sys
from collections import deque

N = int(sys.stdin.readline())
dequee = deque(enumerate(map(int, sys.stdin.readline().split())))
answer = []

while dequee :
    idx, value = dequee.popleft()
    answer.append(idx+1)

    if value > 0 :
        dequee.rotate(-(value-1))
    elif value < 0 :
        dequee.rotate(-value)

print(' '.join(map(str, answer)))

"""
dequee = [3, 2, 1, -3 -1] 이고
enumerate를 사용하면 dequee = [(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)] 이 된다.
그리고 rotate를 사용하면 회전이 가능하다
rotate(1)은 원형 큐를 시계 방향으로 회전, rotate(-1)은 원형 큐를 시계 반대방향으로 회전 한다.
처음 value가 3인데 이때는 이미 pop을 해서 위치가 (1, 2)에 위치해 있다.
value가 양수이므로 오른쪽으로 가야하는데 오른쪽으로 가려면 rotate기준으로는 시계 반대방향을 회전시켜야 오른쪽으로 이동할 수 있다.
반시계방향으로 이동해야해서 -를 붙여주고 pop을 통해 자동으로 한칸 이동됐으므로 -1을 해주므로써 (3, -3)으로 이동할 수 있다.
이제 (3, -3)에서 pop을 해주면 (4,-1)에 위치하게 된다.
여기서 -3임으로 왼쪽으로 3칸 가야하는데 rotate기준 시계방향으로 회전해줘야함으로 rotate()는 양수가 되야한다.
그래서 -3에서 -를 해줘 +로 만들어줘서 시계방향으로 3칸 움직이면 (4, -1)로 이동하게 된다.
이러한 형태로 풀어 문제를 해결할 수 있다.

해당 문제를 풀때 rotate를 이해하는데 한참 걸렸다.
rotate를 할때는 어느 방향으로 회전하는지 생각을 잘하고 문제에 적용해야겠다.
"""