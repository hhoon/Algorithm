n = int(input())
li = []

for i in range(n) :
    li.append(list(map(int, input().split())))

for i in range(1, n) :
    for j in range(len(li[i])) :
        if j == 0 :
            li[i][j] += li[i-1][j]
        elif i == j :
            li[i][j] += li[i-1][j-1]
        else :
            li[i][j] += max(li[i-1][j-1], li[i-1][j])
print(max(li[-1]))

"""
해당문제는 DP를 활용하여 문제를 푸는데
i가 1부터 시작할때 li[i][j]에다가 전에 값을 더해주는 방식으로 문제를 풀었다.
j == 0일때는 제일 왼쪽으로 갈 경우를 다 더해주었고
i == j 의 경우는 제일 오른쪽으로 갈 경우를 다 더해주었다.
그리고 니머지 값들은 두 값(위에 값)을 기준으로 max인것을 더 해주면 모든 경우의 합을 구할 수 있다.
이렇게 구한 후 마지막 값들 중 max를 찾아 문제를 해결 할 수 있었다. 
"""