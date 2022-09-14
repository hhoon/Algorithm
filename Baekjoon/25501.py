def recursion(s, l, r) :
    global cnt
    cnt += 1
    if l >= r :
        return 1
    elif s[l] != s[r] :
        return 0
    else :
        return recursion(s, l+1, r-1)

def isPalindrome(s) :
    return recursion(s, 0, len(s)-1)

T = int(input())

for i in range(T) :
    cnt = 0
    s = input()
    print(isPalindrome(s), cnt)

"""
*변수 cnt
함수 내에서 전역 변수로 cnt를 활용하기 위해서는 global을 사용해야 한다.
문제를 꼼꼼히 읽어보고 풀이를 하자
"""