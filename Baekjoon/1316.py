N = int(input())
group = 0

for i in range(N) :
    word = input()
    error = 0
    for j in range(len(word)-1) :
        if word[j] != word[j+1] :
            word2 = word[j+1:]

            if word2.count(word[j]) > 0 :
                error += 1
    if error == 0 :
        group += 1

print(group)

"""
앞에 나온문자가 뒤에 나오는 경우(연속으로 나오는 경우 제외)를 체크하기 위해
연속으로 나오지 않는 문자부터 슬라이스를 이용하여 다른 변수에 저장하고
그 값을 다른 변수로부터 count 함수를 이용하여 확인을 한다.
조금 더 생각하는 힘을 기르자.
"""