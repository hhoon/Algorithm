while True :
    n = int(input())
    li = []
    for i in range(1, int(n/2+1)) :
        if n % i == 0 :
            li.append(i)
    if n == -1 :
        break
    elif sum(li) == n :
        print(n, "=", end=" ")
        for i in li :
            print(i, end=" ")
            if i != li[-1] :
                print("+", end=" ")
            else :
                print()
    else :
        print(n, "is NOT perfect.")

"""
약수를 구할때는 해당값을 1부터 나눠봐서 나머지가 0이면 약수에 해당한다.
"""