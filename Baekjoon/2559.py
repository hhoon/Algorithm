N, K = map(int, input().split())
li = list(map(int, input().split()))
li = [0] + li
li2 = []
for i in range(N) :
    li[i+1] += li[i]

for j in range(N-K+1) :
    li2.append(li[j+K]-li[j])
print(max(li2))

"""
이중for문을 사용하면 시간초과가 발생한다.
그래서 이전에 풀었던 경험을 토대로 누적합을 구했다.
누적합을 구한 후 규칙을 고민해본 결과 2번째 for문과 같이 표현하면
해당 규칙을 찾을 수 있었다.
계속 생각해보며 규칙을 찾는 연습을 해보는것이 중요한 것 같다.
"""