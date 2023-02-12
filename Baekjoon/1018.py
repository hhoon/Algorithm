N, M = map(int, input().split())
li = []
li2 = []
for i in range(N) :
    li.append(input())

for i in range(N-7) :
    for j in range(M-7) :
        cnt1 = 0
        cnt2 = 0
        for k in range(i, i+8) :
            for l in range(j, j+8) :
                if (k+l) % 2 == 0 :
                    if li[k][l] != 'W' :
                        cnt1 += 1
                    if li[k][l] != 'B' :
                        cnt2 += 1
                else :
                    if li[k][l] != 'B' :
                        cnt1 += 1
                    if li[k][l] != 'W' :
                        cnt2 += 1
        li2.append(min(cnt1, cnt2))
print(min(li2))

"""
해당문제는 우선 8*8로 자른다는 것을 인지해야한다.
해당 입력이 주어졌을때 어디서 8*8로 잘랐을때 최소로 수정해야하는지를 찾는
문제이다.
for문중 N-7, M-7의 뜻은 예를들어 N = 10인 경우는 N-7 = 3이 된다.
for문을 3번돌린다는뜻인데 세로줄을 1번줄부터 시작하는경우, 
2번째, 3번줄부터 시작하는 경우(이렇게해서 3,4번째 for문에서 8번씩하면) 8*8
씩 모든 경우를 다 해볼수가 있다.
그리고 k+l이 중요한데 현재 행의 번호 k, 현재 열의 번호 l의 합이 짝수이면
시작점의 색깔과 같아야 하고, 홀수이면 시작점의 색깔과 다른 색이어야 한다.
이러한 규칙을 이용하면 3, 4번째 for문을 만들수 있게 되고 이후
처음 시작점에서 8*8의 최소값을 li2리스트에 넣어주고 그다음 시작점으로부터
한칸 옆으로 가서 8*8의 최소값을 li2리스트에 넣어주면서 해당 최소값을 모두
구한 후 li2리스트의 최소값을 구해서 답을 구할 수 있게 된다.

해당문제는 많이 어려워 풀이를 봤는데 조금 더 노력해서 해당 문제처럼
코딩을 할 수 있도록 노력해야겠다.
"""