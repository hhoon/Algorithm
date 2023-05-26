import sys

def w(a, b, c) :
    if a <= 0 or b <= 0 or c <= 0 :
        return 1

    elif a > 20 or b > 20 or c > 20 :
        return w(20,20,20)
    
    elif dp[a][b][c] :
        return dp[a][b][c]
    
    elif a < b and b < c :
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    
    else :
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True :
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1 :
        break
    else :
        print("w(%d, %d, %d) = %d" %(a, b, c, w(a,b,c)))

"""
처음 문제에 있는 것을 그대로 파이썬으로 구현하였더니 시간초과가 발생하였다.
해당문제는 dp를 활용하여 이미 계산한 값을 저장하여 증복되는 계산을 줄여 문제를 해결해야 한다.

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
위와 같은 형태로 사용하면 3차원 배열을 만들 수 있다.
그리고 거기에 한번 계산한 값은 저장을 해준다.
이후 dp[a][b][c]가 값이 있다면 해당 값을 return 해주므로써 문제를 해결 할 수 있다.
"""