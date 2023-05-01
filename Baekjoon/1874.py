n = int(input())
li = []
answer = []
num = 1
NO = []

for i in range(n) :
    inputt = int(input())
    while num <= inputt :
        li.append(num)
        answer.append("+")
        num += 1
    if li[-1] == inputt :
        li.pop()
        answer.append("-")
    else :
        NO = ["NO"]
if len(NO) == 1 :
    print("NO")
else :
    for i in answer :
        print(i)

"""
이 문제는 오름차순으로만 들어가고 1부터 n까지 수를 가지고 push(+), pop(-)을 한다.
처음 입력값이 4니까 1부터 4까지 push push push push pop을 해준다.
그리고 다음 입력값이 3이므로 리스트에 제일 마지막인 3을 바로 pop을 해준다.
그 다음 입력값은 6이므로 4와 3을 제외하고 push(5) push(6) pop(6)을 해준다.
이러한 형태로 출력을 하는 문제이다.
처음 문제를 풀때는 if문으로 여러경우의 수를 넣어 풀려고 하니 코드도 지저분하고 답도
제대로 나오지 않았다. 그리고 위와 같은 형태로 문제를 풀때 pop일 경우 num -= 1을
해주었더니 이미 pop된 값들이 중복으로 발생하여 해당부분을 제외해주고 문제를 풀으니
위와 같이 해결 할 수 있었다.
문제를 많이 풀어보며 여러 관점에서 문제 해결하는 힘을 길러야겠다.
"""