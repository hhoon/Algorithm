def solution(brown, yellow):
    answer = []
    yellow_x_plus_y = (brown-4) // 2
    for i in range(yellow_x_plus_y) :
        x, y = i, yellow_x_plus_y-i
        if (x*y) == yellow :
            answer.append(y+2)
            answer.append(x+2)
            break
        
    return answer

"""
해당문제를 풀려면 식을 세워야한다.
우선 갈색 꼭지점 4개를 빼주고 2로 나누면 노란색의 가로의길이 + 세로의길이를 구해줄 수 있다.
그 후에 x*y == yellow를 for문을 통해 구해준다.
예를들어 brown 8이고 yellow가 1인경우
yellow_x_plus_y = 2이 된다.
이런경우 위와 같이 for문을 돌리면
0 * 2
1 * 1 == 1 이다.
그리고 높은 수가 가로를 먼저 출력해줘야하기 때문에 y + 2(꼭지점 가로)
x + 2(꼭지점 세로)를 넣어주어 문제를 해결할 수 있다.
"""