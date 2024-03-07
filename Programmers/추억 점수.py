def solution(name, yearning, photo):
    answer = []
    dict = {}
    
    for i in range(len(name)) :
        dict[name[i]] = yearning[i]
        
    for j in photo :
        sum = 0
        for k in j :
            if k in dict :
                sum += dict.get(k)
        answer.append(sum)
        
    return answer