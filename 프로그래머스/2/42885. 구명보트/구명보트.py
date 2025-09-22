"""
최대 2명, 무게 제한 O

"""

def solution(people, limit):
    answer = 0
    
    people.sort()
    right = len(people) - 1
    left = 0
    
    while (right >= left):
        temp = people[right]
        if (temp + people[left] <= limit):
            left += 1
        right -= 1
        answer += 1
    return answer