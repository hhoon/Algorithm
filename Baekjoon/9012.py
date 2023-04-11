N = int(input())
for i in range(N) :
    li = input()
    cnt_left = 0
    cnt_right = 0

    if li.count("(") == li.count(")") :
        for i in range(int(len(li))) :
            if li[i] == "(" :
                cnt_left += 1
            else :
                cnt_right += 1
            if cnt_left < cnt_right :
                print("NO")
                break
            if i == int(len(li)-1) :
                print("YES")
    else :
        print("NO")

"""
처음에는 '(' 와 ')'의 갯수가 같은경우는 yes로 하여 풀었는데
'())(()' 이 경우는 갯수가 같아도 NO가 나와야 했다.
그래서 규칙을 찾아보니 앞에서부터 순서대로 입력할때 '('의 갯수보다
')'의 갯수가 많아지는 순간 문제에서 요구하는 VPS가 아니게 되었다.
그래서 cnt를 활용하여 해당 문제를 해결할 수 있었다.
"""