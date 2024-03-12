def solution(answers):
    answer = []
    student1 = [1,2,3,4,5] * (10000 // 5)
    student2 = [2,1,2,3,2,4,2,5] * (10000 // 8)
    student3 = [3,3,1,1,2,2,4,4,5,5] * (10000 // 10)
    std1 = 0
    std2 = 0
    std3 = 0
    
    for i in range(len(answers)) :
        if answers[i] == student1[i] :
            std1 += 1
        if answers[i] == student2[i] :
            std2 += 1
        if answers[i] == student3[i] :
            std3 += 1
            
    maxx = max(std1, std2, std3)
    if maxx == std1 :
        answer.append(1)
    if maxx == std2 :
        answer.append(2)
    if maxx == std3 :
        answer.append(3)
        
    return answer

"""
학생마다 정답을 몇문제까지 맞췄는지까지는 해결하였으나 마지막 maxx부터인 많이 맞춘 순서 및
오름차순으로 출력하는 방법을 생각하지 못했다.
위처럼 if문을 사용하여 append로 숫자를 넣어주어 문제를 쉽게 해결할 수 있었다.
조금 더 많이 문제를 풀어봐야겠다.
"""