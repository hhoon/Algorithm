T = int(input())
li = []

for i in range(T) :
    li.append(int(input()))
maxx = max(li)
prime = [False, False] + [ True for i in range(maxx-1) ]

for i in range(2, int(maxx**(1/2))+1) :
    if prime[i] :
        for j in range(i+i, maxx+1, i) :
            if prime[j] :
                prime[j] = False

for i in li :
    cnt = 0
    for j in range(2, (i//2)+1) :
        if prime[j] and prime[i-j] :
            cnt += 1
    print(cnt)

"""
prime = [False, False] + [ True for i in range(maxx-1) ]의 의미는
처음에 False, False을 0, 1에 넣고 2번부터 True를 넣는다는 뜻이다.

에라토스테네스의 체를 아래와 같이도 표현 할 수 있다고 한다.
for i in range(2, int(maxx**(1/2))+1) :
    if prime[i] :
        for j in range(i+i, maxx+1, i) :
            if prime[j] :
                prime[j] = False

해당 문제를 풀기 위해 입력 값중 maxx값을 구해 해당 값까지 에라토스테네스의 체를 사용하여 소수를
구해주었다.

    for j in range(2, (i//2)+1) :
        if prime[j] and prime[i-j] :
            cnt += 1
여기서 i//2가 뜯하는것은 3 5나 5 3 이 같기 때문에 중복을 방지해주기 위해 2로 나누었다.
그리고 prime[j] and prime[i-j]의 뜻은
예를들어 8의 소수의 합을 구할 경우
prime[3]이 소수이고 prime[5]도 소수이면 카운트를 1 더하라는 뜻이다.
"""