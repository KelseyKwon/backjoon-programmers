"""
뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 가능

100 - speeds[i] -> 
remain_days = [7, 3, 9] -> 7 > 3 -> 같이... 3 < 9 뒤에...
remain_days = [5, 10, 1, 1, 20, 1] -> 1, 3, 2
"""
import math
def solution(progresses, speeds):
    answer = []
    nums = len(progresses)
    remain_days = []
    
    for i in range(nums):
        remain_day = math.ceil((100 - progresses[i]) / speeds[i])
        remain_days.append(remain_day)
        
    prev_day = remain_days[0]
    count = 1
    for i in range(1, nums):
        print(remain_days[i])
        if (prev_day >= remain_days[i]):
            count += 1
        else:
            prev_day = remain_days[i]
            answer.append(count)
            count = 1
    answer.append(count)
    return answer