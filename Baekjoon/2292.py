N = int(input())
count = 1
six = 1
while six < N :
    six += 6 * count
    count += 1

print(count)

"""
규칙을 먼저 찾는게 중요하다!
지나가야하는 방의 개수 1 : 1
지나가야하는 방의 개수 2 : 2, 3, 4, 5, 6, 7
지나가야하는 방의 개수가 6의 배수로 증가하는것을 알 수 있다.
"""