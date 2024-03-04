def solution(array, commands):
    answer = []
    
    for a in commands :
        tmp = []
        i = a[0]-1
        j = a[1]-1
        k = a[2]-1
        for b in range(len(array)) :
            if i <= b and b <= j:
                tmp.append(array[b])
            tmp = sorted(tmp)
        answer.append(tmp[k])
    return answer