N = int(input())
M = []
for i in range(N, 0, -1) :
    sum = i
    for j in str(i) :
        sum += int(j)
    if sum == N :
        M.append(i)

if not M  :
    print(0)
else :
    print(min(M))

"""
문제를 풀때 포기하지 말고 좀 더 생각해보려고 노력해보자
리스트가 비어 있는지 확인할때는
if not li와 같이 표현하면 해당 리스트가 비어있는지
확인할 수 있다.
"""