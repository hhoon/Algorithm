from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    dic = defaultdict(int)
    total = 0
    
    for i in tangerine :
        dic[i] += 1
    dic = sorted(dic.items(), key = lambda x : x[1])
    dic.reverse()
    
    for j in dic :
        answer += 1
        total += j[1]
        if total >= k :
            break
    
    return answer

"""
해당문제를 풀기 위해서는 딕셔너리를 사용해야한다.
dic = defaultdict(int)를 사용해서 default값을 넣을 수 있고 이를 기반으로 dic[i]가 확인될때마다 1을 더해서 카운트를 할 수 있다.
(처음에 count함수를 사용했더니 시간초과 발생)
그리고 람다식을 사용하면 정렬할 수 있는데 이때는 dic.items()를 기반으로 람다식을 사용하여 정렬할 수 있다. 
이렇게 정렬한 값을 기반으로 k값과 비교해주면 문제를 해결할 수 있다. 

위와 같은 유형의 문제들을 많이 풀어 여러 유형을 숙지해야겠다.
"""