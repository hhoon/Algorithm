N = int(input())
li = []
for i in range(N) :
    li.append(input())

se = set(li)
li = list(se)
li.sort()
li.sort(key=len)

for i in li :
    print(i)

"""
리스트의 중복을 제거하기 위해서는 set함수를 사용하면 된다.
그리고 sort함수에 key를 사용하면 길이별로도 정렬이 가능하다.
"""