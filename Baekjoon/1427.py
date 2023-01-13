N = list(map(int,input()))
N.sort()
N.reverse()

for i in N :
    print(i, end="")

"""
list에 input().split()가 아닌 input()을 사용하면 123 입력시 1, 2, 3
각각 따로따로 입력되어 저장이 된다.
숫자를 정렬하기 위해 sort()를 사용하기 전에는 해당 list의 요소들이 int형
인지 확인 후 sort()를 사용하자.
sort() 사용후 reverse 사용하면 정렬된 상태로 reverse가 적용 가능하다.
"""