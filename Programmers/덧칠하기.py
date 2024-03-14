def solution(n, m, section):
    answer = 1
    paint = section[0]
    for i in range(0, len(section)) :
        if section[i] - paint >= m :
            answer += 1
            paint = section[i]
    return answer

"""
처음에 한번은 무조건 칠해주기 때문에 answer에 1을 넣어주고,
section[i] - 시작점(paint)이 페인트길이(m)를 넘은 순간
페인트를 한번 더 칠해줘야하기 때문에 answer에 1을 더해주고 시작점을 다시 설정해준다.
이렇게 접근하면 문제를 해결할 수 있다.

알고리즘을 많이 풀어봐서 문제 해결 능력을 키워야겠다.
"""