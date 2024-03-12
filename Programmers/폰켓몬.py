def solution(nums):
    answer = 0
    half = len(nums)/2
    nums = set(nums)

    if len(nums) < half :
        answer = len(nums)
    else :
        answer = half
    return answer