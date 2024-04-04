from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons, len(dungeons)) :
        cnt = 0
        p = k
        for j in i :
            if p >= j[0] :
                p -= j[1]
                cnt += 1
        answer = max(answer, cnt)
            
    return answer

"""
해당 문제를 해결하기 위해서는 permutations를 사용하여 모든 경우의 수를 비교하여 각 경우의
수마다 피로도를 소모시켜 확인을 할 수 있었다.
"""