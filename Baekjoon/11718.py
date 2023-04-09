for i in range(100) :
    try :
        s = input()
        print(s)
    except :
        continue

"""
처음 try except문을 사용하지 않고 문제를 풀었더니 계속 런타임 에러가
발생하였다.
횟수가 주어지지 않은 위의 문제는 try except문을 통해 문제를 해결할 수 있었다.
"""