n = int(input())
print(int((n-2)*(n-1)*n / 6))
print(3)

"""
첫번째 for문 1일때
두번째 for문 2일때
세번째 for문 3 ~ 7 = 5개

두번째 for문 3일때
세번째 for문 4 ~ 7 = 4개

두번째 for문 4일때
세번째 for문 5 ~ 7 = 3개
...
첫번째 for문 1일때 (5,4,3,2,1)
첫번째 for문 2일때 (4,3,2,1)
            3일때 (3,2,1)
            4일때 (2,1)
            5일때 (1)
            총합 = 35
식으로 표현하면 nC3 이고 이는
(n-2)(n-1)n / 6 으로 표현할수 있다고 한다.
"""