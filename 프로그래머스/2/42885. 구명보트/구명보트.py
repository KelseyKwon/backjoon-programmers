"""
구명보트에는 최대 2명까지만

일단 무거운 사람은 무조건 한명 태울 수 있어 -> 근데, 가벼운 사람도 태울 수 있냐 없냐가 
"""

def solution(people, limit):
    answer = 0
    people.sort()
    
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if (people[right] + people[left] <= limit):
            left += 1
        right -= 1
        answer += 1
    return answer