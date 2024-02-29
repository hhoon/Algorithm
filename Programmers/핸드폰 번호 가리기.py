def solution(phone_number):
    answer = ''
    front = (len(phone_number) - 4)
    for i in range(len(phone_number)) :
        if i < front :
            answer += '*'
        else :
            answer += str(phone_number[i])
    return answer