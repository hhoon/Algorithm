T = int(input())

for i in range(T) :
    floor = int(input())
    room = int(input())
    zero = [a for a in range(room+1)]

    for j in range(1, floor+1) :
        for k in range(1, room+1) :
            zero[k] += zero[k-1]
    print(zero[-1])

"""
zero = [a for a in range(room+1)] 이러한 형식으로 사용하면 원하는 입력값
만큼 리스트의 객체를 입력할 수 있다.
이 문제는 먼저 0층의 room번방까지를 만들어 놓는다
(0 1 2 3 4 5...)
floor가 2층이고 3호의 인원을 찾는다고 가정해보자
이후 위의 for문을 돌려보면
1층 1호 zero[1] = 1(zero[1]) + 0(zero[0]) = 1
1층 2호 zero[2] = 2(zero[2]) + 1(zero[1]) = 3
1층 3호 zero[3] = 3(zero[3]) + 3(zero[2]) = 6
이렇게 하면 1층의 3호까지의 데이터 입력되게 된다.
2층 1호 zero[1] = 1(zero[1]) + 0(zero[0]) = 1
2층 2호 zero[2] = 3(zero[2]) + 1(zero[1]) = 4
2층 3호 zero[3] = 6(zero[3]) + 4(zero[2]) = 10 이 된다.
즉, 규칙을 찾아보면 2층의 3호의 경우 = 1층의 3호 + 2층의 2호를 더해 구할 수
있고 바로 직전층의 같은 호실의 값을 zero[k] += zero[k-1] 와 같은 식을
사용하면 사용할 수 있고 현재층으로 갱신도 가능하다.
그리고 zero[-1]을 사용하여 가장 마지막 값을 확인할 수 있었다.

위와 같은 식을 생각하지 못하여 찾아 보았고 이해하는데도 시간이 조금 걸렸다.
수학적 사고를 기르는 노력을 해보자.
"""