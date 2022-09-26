N = int(input())
num = list(map(int, input().split()))
sum = 0

for i in range(N) :
    cnt = 0
    for j in range(num[i]) :
        if num[i] != 1 :
            if num[i] % (j+1) == 0 :
                cnt += 1
    if cnt == 2 :
        sum += 1

print(sum)

"""
소수는 1을 제외하고 1과 자기자신만을 약수로 가지는 자연수를 의미한다.
ex) 3(1,3), 5(1,5)...   약수가 2개
5가 소수인지 확인하는 방법은 1, 2, 3, 4, 5를 전부 5로 나눠서 나머지가
0인 경우가 2개인 경우만 소수로 계산을 하면 된다.
"""