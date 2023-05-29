N, K = map(int, input().split())
li = list(map(int, input().split()))

def merge_sort(li) :
    if len(li) == 1 :
        return li
    
    li2 = []
    i, j = 0, 0

    mid = (len(li) + 1) // 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])

    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            li2.append(left[i])
            ans.append(left[i])
            i += 1            

        else :
            li2.append(right[j])
            ans.append(right[j])
            j += 1

    while i < len(left) :
        li2.append(left[i])
        ans.append(left[i])
        i += 1
    
    while j < len(right) :
        li2.append(right[j])
        ans.append(right[j])
        j += 1

    return li2

ans = []
merge_sort(li)

if len(ans) > K :
    print(ans[K-1])
else :
    print(-1)

"""
merge_sort함수 중간에
    mid = (len(li) + 1) // 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])
이부분의 재귀함수를 이용하여 문제를 해결할 수 있다.
4 5 1 3 2 라고 가정했을때
첫 left는 4 5 1 right는 3 2가 된다.
이후 재귀를 통해 4 5 / 1로 되고 또 한번 재귀를 통해

4 / 5가 된다.
4와 5를 비교해서 순서대로 li2에 넣어준다

그 다음 4 5 / 1
수를 비교 하여 1 4 5 순으로 넣어 준다.

다음은 3 / 2 이다.
수를 비교하여 2 3 순으로 넣어 준다.

여기까지하면 함수의 return li2이기 때문에
left = merge_sort(li[:mid]) = [1, 4, 5]가 되고
right = merge_sort(li[mid:]) = [2, 3]이 된다.

이후 수를 비교하면
li2 = [1, 2, 3 ,4, 5]가 된다.
ans에는 비교할때마다 수를 넣어주기 때문에 그 기록이 저장된다.
ans = [4, 5, 1, 4, 5, 2, 3, 1, 2, 3, 4, 5] 이다.
인덱스가 0부터 시작이므로 k-1을 해주므로써 정답을 구할 수 있다.

재귀함수의 흐름을 이해하는데 어려움이 있다.
문제를 많이 풀어 이를 보완 해야겠다.
"""