def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)) :
        if arr[i] != arr[(i-1)] :
            answer.append(arr[i])
    return answer

"""
처음 문제를 접근할때는 del arr[i]와 같은 방법을 풀려고 했는데
그렇게 되면 list의 범위가 벗어나는 오류가 발생했다.
그래서 answer 배열에 첫값을 넣어주고 중복되지 않았을때 값을 바로바로 넣어 줌으로써
문제를 해결할 수 있었다.
"""