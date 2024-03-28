key = []
for i in range(9) :
    key.append(int(input()))
summ = sum(key)
for i in range(len(key)) :
    if len(key) == 7 :
        break
    for j in range(i+1,len(key)) :
        if summ - (key[i]+key[j]) == 100 :
            a = key[i]
            b = key[j]
            key.remove(a)
            key.remove(b)
            break
key.sort()
for i in key :
    print(i)

"""
처음 문제를 풀어서 맞았다고 생각했는데 계속 채점결과 틀린답이 나왔다.
처음에는 for j 부분만 break를 해줘서 안쪽만 멈추고 뒤쪽 for문은 멈추지 않았기 때문에
틀린답이 나온것이었다. 그래서 바깥쪽 for문에도 break를 걸어서 문제를 해결할 수 있었다.
"""