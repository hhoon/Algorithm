from itertools import product

def solution(word):
    alpha = ['A','E','I','O','U']
    dic = []
    answer = 0
    
    for i in range(1,6) :
        for j in product(alpha, repeat=i) :
            dic.append(''.join(j))
    dic.sort()
    answer = dic.index(word) + 1
    
    return answer

"""
해당문제는 product 함수를 사용하여 해결할 수 있었다.
product 함수를 사용하여 반복을 i번 한 후 sort로 정렬을 해줌으로써 원하는 형태로 리스트를
만들 수 있었고 index를 사용하여 답을 구할 수 있었다.
"""