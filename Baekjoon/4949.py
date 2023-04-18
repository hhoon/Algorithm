while True :
    s = input()
    li = []

    if s == '.' :
        break
    else :
        for i in s :
            if i == '(' or i == '[' :
                li.append(i)
            elif i == ')' :
                if len(li) != 0 and li[-1] == '(' :
                    li.pop()
                else :
                    li.append(i)
                    break
            elif i == ']' :
                if len(li) != 0 and li[-1] == '[' :
                    li.pop()
                else :
                    li.append(i)
                    break
    if len(li) == 0 :
        print("yes")
    else :
        print("no")

"""
해당 문제를 풀때 계속해서 한 두가지의 경우의 수를 생각하지 못해 원하는 결과값이 나오지 않았다.
하지만 위와 같이 '(' or '[' 일 경우 append()를 해주고
마지막에 저장된 문자와 ')' or ']'로 같을때 이미 저장된 문자를 pop()을 해주므로써
문제를 해결 할 수 있었다.
len(li) != 0을 처음에는 작성하지 않았는데 그렇게 하니 li[-1]에서 오류가 나서
넣어준다는 것을 알았다.
"""