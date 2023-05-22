word = list(input())
reverse = list(reversed(word))
if word == reverse :
    print(1)
else :
    print(0)

"""
word.reverse()로 표현하여 문제를 풀때 계속 원하는 답이 나오지 않아
print로 word.reverse()를 확인해보니 None 값이 나왔다.
reverse함수는 리스트 값을 반환하는 것이 아니라 변환시켜주므로 None이
출력 된다고 한다.
그래서 reversed라는 내장함수(list에서 제공하는 함수 아님)을 사용하여
문제를 해결할 수 있었다.
"""