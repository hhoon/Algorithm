N, M = map(int, input().split())
li = []

def Backtracking() :
    if len(li) == M :
        print(" ".join(map(str, li)))
        return
    
    for i in range(1, N+1) :
        if len(li) != 0 and i < li[-1] :
            continue
        li.append(i)
        Backtracking()
        li.pop()

Backtracking()