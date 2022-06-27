a, b, v = map(int, input().split())
day = (v-b) / (a-b)

if day > int(day) :
    day = int(day) + 1
print(int(day))

"""
처음 코딩한 것
while True :
    height += a
    day += 1
    if height < v :
        height -= b
    
    else :
        print(day)
        break;
하지만 큰 수를 넣었을시 시간이 오래걸리므로 문제의 조건에 부합하지 못함
하지만 day = (v-b) / (a-b)라는 공식을 사용하면
반복문을 사용하지 않고도 값을 구할 수 있다.
나무 높이를 기준으로 하는 식을 작성해보면 (a-b)*n +  = v와 같다.
a만큼 올랐다 b만큼 떨어지기를 반복하기 때문에 a-b의 거림만큼 올라가는 것을
n만큼 반복하고 마지막날에는 a만큼 올라가고서 더 이상 떨어지지 않기 때문이다.

수학식으로 표현해보는 연습을 해보자.
"""