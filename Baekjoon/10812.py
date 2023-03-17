N, M = map(int, input().split())
li = []
for i in range(1,N+1) :
    li.append(i)

for a in range(M) :
    i, j, k = map(int, input().split())
    for b in range(j-k+1) :
        tmp = li[k-1+b]
        li.remove(tmp)
        li.insert(i-1+b, tmp)
for i in li :
    print(i, end = " ")

"""
해당문제를 풀기 위해서는 먼저 문제를 이해해야하는데
입력값의 1 6 4는
12345678910에서 4번째 숫자부터 6번째 숫자까지 1번째 숫자 앞으로 보내라는 뜻이다.
그러면 12345678910 -> 45612378910 된다.
그 다음 입력값은 3 9 8
45612378910에서 8번째 숫자부터 9번째 숫자까지 3번째 숫자 앞으로 보내라는 뜻이다.
그러면 45896123710이 된다.
위와 같은 방법으로 하면 아래와 같이 진행이 된다.
123456 78910
45 6123789 10
4 5896123710
461 23710589
1 46237 10589
해당문제를 풀기 위해 해당값을 remove하고 해당위치에 insert하는 방법으로
문제를 풀었다.
"""