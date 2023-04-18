a, b, c = map(int, input().split())
li = [a, b, c]
maxx = max(li)
two_line = sum(li) - maxx

if maxx >= two_line :
    print(two_line+two_line-1)
else :
    print(sum(li))

"""
삼각형이 성립하려면 가장 긴변의 길이가 남은 두변의 합보다 크거나 같으면 안된다.
가장 긴변 >= 나머지 두변의 합 (삼각형 성립 안함)
가장 긴변 < 나머지 두변의 합 (삼각형 성립)
위와 같은 성질을 이용하여 문제를 해결 하였다.
"""