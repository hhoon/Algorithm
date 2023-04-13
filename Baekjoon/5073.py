while True :
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0 :
        break
    else :
        maxx = max(a, b, c)
        summ = a + b + c
        if (summ - maxx) <= maxx :
            print("Invalid")
        elif a == b == c :
            print("Equilateral")
        elif a != b and b != c and c != a :
            print("Scalene")
        else :
            print("Isosceles")

"""
처음에는 모든 경우를 구해서 풀려고 했는데 효율적이지 못한거 같아 세변의 합을
구하는 방식으로 문제를 해결하였다.
생각을 조금 더 하다보면 효율성이 좋은 코드를 만들수 있으니 조금 더 생각하며
코드를 짜보자.
"""