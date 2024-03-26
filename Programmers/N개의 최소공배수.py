import math

def solution(arr):
    answer = arr[0]
    for i in range(1,len(arr)) :
        gcdd = math.gcd(answer, arr[i])
        answer = (answer * arr[i]) // gcdd
    return answer

"""
여러수의 최소공배수를 구하는 방법중 하나는 두수를 비교하여 최소공배수를 구하고 그 최소공배수와
다음 수의 최소공배수를 구하는 방법으로 배열에 있는 값을 끝까지 구하면 여러수의 최소공배수를
구할 수 있다고 한다.
"""