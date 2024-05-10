def solution(numbers, target):
    answer = 0
    all = [0]
    for i in numbers :
        tmp = []
        for j in all :
            tmp.append(i + j)
            tmp.append((-1*i) + j)
        all = tmp
    for k in all :
        if target == k :
            answer += 1
    
    return answer

"""
해당문제는 bfs를 통해서 해결했는데 all에 모든 경우의수를 다 저장하여 target과 비교하여
답을 구하였다.
bfs를 푸는방법도 여러 방법이 있는것 같아 여러문제를 풀어봐야겠다.
"""