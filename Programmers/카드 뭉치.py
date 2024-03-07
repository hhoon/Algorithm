def solution(cards1, cards2, goal):
    answer = ''
    c1 = 0
    c2 = 0
    for i in range(len(goal)) :
        if goal[i] == cards1[c1] :
            if len(cards1)-1 != c1 :
                c1 += 1
        elif goal[i] == cards2[c2] :
            if len(cards2)-1 != c2 :
                c2 += 1
        else :
            answer = 'No'
            break
        if i == len(goal)-1 :
            answer = 'Yes'
            
    return answer