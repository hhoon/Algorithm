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