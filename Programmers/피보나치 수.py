def solution(n):
    answer = 1
    a = 0
    b = 1
    for i in range(2, n+1) :
        c = a + b
        a = b
        b = c
    answer = c % 1234567
        
    return answer

"""
문제에 1234567으로 나눈 나머지를 리턴하라고 했는데 이를 누락해서 몇개의 케이스에서 실패를 했다.
이번 문제와 같이 규칙을 찾는 연습을 하고, 문제를 잘 파악해야겠다.
"""