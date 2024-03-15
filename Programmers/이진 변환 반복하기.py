def solution(s):
    answer = []
    zero = 0
    cnt = 0
    
    while True :
        tmp = []
        tmp2 = ''
        for i in s :
            if i == '0' :
                zero += 1
            else :
                tmp.append(i)
        cnt += 1
        
        for j in tmp :
            tmp2 += j
            
        s = str(bin(len(tmp2))[2:])

        if len(s) == 1 :
            answer.append(cnt)
            answer.append(zero)
            break
    return answer

"""
문제를 잘못 읽어 문제를 해결하는데 계속 오답이 나왔다.
문제에서 2. x의 길이라고 명시해주고 이것을 2진변환 하라고 했는데 그렇게 하지 않아 계속해서
시간초과가 발생했다.
bin함수를 사용하면 10진법을 2진법으로 변경이 가능하다.

문제를 꼼꼼히 읽고 bin함수 등을 이용하는 엽습을 하자.
"""