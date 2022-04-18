def hansu(n):
    han = []

    for i in range(1,n+1) :
        num1 = 0
        num2 = 0
        if i < 100 :
            han.append(i)
        else :
            num1 = int(str(i)[2]) - int(str(i)[1])
            num2 = int(str(i)[1]) - int(str(i)[0])
            if num1 == num2 :
                han.append(i)
    return len(han)

n = int(input())
print(hansu(n))

"""
설명
등차수열은 말 그대로 같은 차이를 갖는 수열을 뜻함
ex) 1, 3, 5, 7, 9, ...

1 ~ 99까지는 등차수열인지를 판단할 자리 수가 없기 때문에 모두 한수가 성립 된다.
"""