def solution(nums):
    answer = 0
    num = 0
    check = []
    for i in range(len(nums)-2) :
        for j in range(i+1, len(nums)-1) :
            for k in range(j+1, len(nums)) :
                num = nums[i] + nums[j] + nums[k]
                check.append(num)
    for l in check :
        cnt = 0
        for m in range(2, int(l**(1/2))+1) :
            if l % m == 0 :
                cnt += 1
                break
        if cnt == 0 :
            answer += 1

    return answer