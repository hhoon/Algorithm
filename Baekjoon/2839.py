N = int(input())
answer = 0
three_sugar = 0

while True :
    mod = N % 5
    if mod == 0 :
        answer = ((N//5)+three_sugar)
        print(answer)
        break

    N -= 3
    three_sugar += 1

    if N < 0 :
        print(-1)
        break

"""
처음에는 if문을 여러개 사용해서 문제를 풀려 했으나 5kg을 최대치로 사용하는
경우만 있는게 아니어서 값이 다르게 나옴 ( ex) five_mod % 5 )
while문을 사용하여 나머지가 0이 아닌 경우 N에서 3씩 빼서 계산하여
문제의 답을 찾을 수 있었음

수학적으로 생각하는 힘을 더 길러야함
"""