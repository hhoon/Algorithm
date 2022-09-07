input = list(map(int, input().split()))
calc = []
for i in range(6) :
    if i < 2 :
        calc.append(1 - input[i])
    elif 1 < i < 5 :
        calc.append(2 - input[i])
    elif i == 5 :
        calc.append(8 - input[i])
for j in range(6) :
    print(calc[j], end = " ")