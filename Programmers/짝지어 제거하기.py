def solution(s):
    answer = 0
    stack = []
    i = 0
    for i in s :
        if len(stack) == 0 :
            stack.append(i)
        elif stack[-1] == i :
            stack.pop()
        else :
            stack.append(i)
    if len(stack) == 0 :
        answer = 1
    else :
        answer = 0

    return answer

"""
처음 문제 해결시 for문과 if문만을 사용하여 문제를 해결하려 했는데 잘 되지 않아 찾아보니
스택과 팝을 사용하여 접근하면 원하는 결과값과 효율성부분에서도 좋은 결과를 나올수 있음을
알게 되었다.
위와 같은 유형은 스택과 팝을 사용하여 접근하도록 해야겠다.
"""