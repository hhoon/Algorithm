N, M = map(int, input().split())
li = []

def BackTracking() :
    if len(li) == M :
        print(" ".join(map(str, li)))
        return

    for i in range(1, N+1) :
        if i in li :
            continue
        elif len(li) != 0 and i < li[-1]:
            continue
        li.append(i)
        BackTracking()
        li.pop()
BackTracking()

"""
백트레킹이란?
조건에 맞는 해를 만들다가, 아니다 싶으면 뒤로가기해서 다른 방법을 만드는 방법이다.
그래서 대부분 재귀를 이용해서 많이 문제를 해결한다.

위 문제에서는 i in li : continue를 통해 중복문제를 해결 할 수 있었고, 첫 if문의 return을 통해 해당 함수를 빠져나갈 수 있었다.
그리고 pop을 통해 끝에를 지워주며 문제를 풀 수 있었다.
15649번 문제와 유사한데 이번 문제에는 elif문으로 조건을 하나 더 걸어주어 문제를 해결할 수 있었다.

특정 개념의 알고리즘을 풀때는 해당 알고리즘을 공부 후 풀도록 하자.
"""