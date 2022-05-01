T = int(input())

for i in range(T) :
    RSlist = list(input().split())
    R = int(RSlist[0])
    S = RSlist[1]
    text = ""

    for j in range(len(S)) :
        print(S[j]*R, end ="")
    print(end = "\n")



"""
R,S = input().split() 으로도 가능
end를 사용하기보다 text += S[j]*R 이렇게 코딩하는게 깔끔함
"""