S = input()
low = S.lower()
settemp = set(low)
temp = list(settemp)
temp2 = []   #cnt

for i in range(len(temp)):
    cnt = low.count(temp[i])
    temp2.append(cnt)

if temp2.count(max(temp2)) > 1 :
    print("?")

else :
    addr = temp2.index(max(temp2))
    print(temp[addr].upper())


"""
set함수를 사용해서 알파벳의 중복을 제거해줘야 문제를 해결할 수 있음
중복을 제거하고 count를 새서 max가 하나 이상이면 '?' 출력
lower(), upper()를 이용하여 소문자 대문자로 변경 가능
"""