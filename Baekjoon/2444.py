N = int(input())
star = 1
space = (N-1)
for i in range(2*N-1) :
    if i < N-1 :
        print(" "*space + "*"*star)
        star += 2
        space -= 1
    else :
        print(" "*space + "*"*star)
        star -= 2
        space += 1
    
    """
    해당문제를 풀때 계속해서 띄어쓰기가 한칸씩 더 되었는데 이유를
    찾아보니 print(" "*space, "*"*star) 사이에 ,를 사용하니 한 칸의
    띄어쓰기가 작용하여 계속해서 한 칸씩 더 띄어쓰는 문제가 있었다.
    이후에는 이런 실수를 하지 않도록 주의하자
    """