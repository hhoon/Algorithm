def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n) :
        li = []
        for j in range(n) :
            if arr1[i] % 2 == 1 or arr2[i] % 2 == 1 :
                li.append("#")
            else :
                li.append(" ")
            arr1[i] = arr1[i] // 2
            arr2[i] = arr2[i] // 2
        li.reverse()
        tmp = ""
        for k in li :
            tmp += k
        answer.append(tmp)
    return answer
"""
처음에는 아래와 같이 길게 문제를 풀었더니 원하는 출력값은 얻었지만 시간초과가 발생했다.
위와 같이 코딩을 하면 훨씬 간결하고 속도가 빠르게 설계할 수 있다.
간결하고 속도가 빠르게 알고리즘을 해결하는 연습을 해야겠다.

def solution(n, arr1, arr2):
    answer = []
    arr1_2 = []
    arr2_2 = []
    for i in arr1 :
        tmp = []
        while True :
            if i == 1 :
                tmp.append(1)
                if len(tmp) < n :
                    for l in range(n-len(tmp)) :
                        tmp.append(0)
                    tmp.reverse()
                    arr1_2.append(tmp)
                    break
                else :
                    tmp.reverse()
                    arr1_2.append(tmp)
                    break
            k = i % 2
            tmp.append(k)
            i = i // 2
    for i in arr2 :
        tmp = []
        while True :
            if i == 1 :
                tmp.append(1)
                if len(tmp) < n :
                    for l in range(n-len(tmp)) :
                        tmp.append(0)
                    tmp.reverse()
                    arr2_2.append(tmp)
                    break
                else :
                    tmp.reverse()
                    arr2_2.append(tmp)
                    break
            k = i % 2
            tmp.append(k)
            i = i // 2

    for i in range(len(arr1_2)) :
        tmp = ""
        for j in range(n) :
            if arr1_2[i][j] == 1 or arr2_2[i][j] == 1 :
                tmp += "#"
            else :
                tmp += " "
        answer.append(tmp)
    return answer
"""