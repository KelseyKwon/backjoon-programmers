import math

def solution(progresses, speeds):
    answer = []
    
    # ceil((100 - 93) / 1)
    # 7, 3, 9
    # while 더 작을때까지 ++
    
    # 5, 10, 1, 1, 20, 1
    days = []
    
    for i in range(len(progresses)):
        # [7, 3, 9]
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    flag = days[0]
    count = 1
    for i in range(1, len(days)):
        if flag < days[i]:
            flag = days[i]
            answer.append(count)
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer