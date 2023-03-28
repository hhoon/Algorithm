T = int(input())

for i in range(T) :
    Quarter = 25
    Dime = 10
    Nickel = 5
    Penny = 1
    Cent = int(input())

    if Cent // Quarter > 0 :
        A = Cent // Quarter
        Cent -= Quarter*A
    else :
        A = 0
    if Cent // Dime > 0 :
        B = Cent // Dime
        Cent -= Dime*B
    else :
        B = 0
    if Cent // Nickel > 0 :
        C = Cent // Nickel
        Cent -= Nickel*C
    else :
        C = 0
    if Cent // Penny > 0 :
        D = Cent // Penny
    else :
        D = 0
    print(A, B, C, D)