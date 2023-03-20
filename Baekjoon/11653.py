N  = int(input())
i = 2
li = []
while True :
        if N % i == 0 :
                N = N / i
                li.append(i)
        elif N <= i :
                break
        else :
                i += 1
for i in li :
        print(i)