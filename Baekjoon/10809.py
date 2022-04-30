S = input()
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(abc)):
    if abc[i] in S :
        print(S.index(abc[i]), end =" ")
    else :
        print(-1, end = " ")


"""
index를 활용하여 위치를 찾을 수 있음
end를 활용하면 개행문자 대신 원하는 문자 출력
"""