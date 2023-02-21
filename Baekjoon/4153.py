li = []
while True :
        li = list(map(int, input().split()))
        if li[0] == 0 & li[1] == 0 & li[2] ==0 :
                break
        maxx = max(li)
        li.remove(maxx)
        if maxx * maxx == (li[0] * li[0]) + (li[1] * li[1]) :
                print("right")
        else :
                print("wrong")

"""
세변이 주어졌을때 직각삼각형의 성질에 따라 (가장긴변의 제곱 = 나머지 두변들의 제곱의 합 ex) a제곱 = b제곱 + c제곱) 이라고 한다.
처음 문제를 풀때 a제곱 = b제곱 + c제곱 이렇게 식을 세워 풀었더니 채점결과 틀렸었다.
문제를 해결하기 위해 다시 봐보니 a제곱 = b제곱 + c제곱 이렇게 문제를 풀게 되면 입력시 가장 긴변의 위치가 고정되게 입력해야해서 오답이 나왔다.
해당 문제를 해결하기 위해 위와 같이 다시 식을 세워 문제를 해결할 수 있었다.
"""