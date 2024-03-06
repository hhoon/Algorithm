def solution(a, b):
    answer = ''
    day = {1:'FRI', 2:'SAT', 3:'SUN', 4:'MON', 5:'TUE', 6:'WED', 7:'THU'}
    date = 0
    day_calc = 0
    for i in range(1,a+1) :
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12 :
            date = 31
        elif i == 2 :
            date = 29
        else :
            date = 30
        for j in range(1, date+1) :
            day_calc += 1
            if i == a and j == b :
                answer = day.get(day_calc)
                break
            if day_calc == 7 :
                day_calc = 0
    return answer