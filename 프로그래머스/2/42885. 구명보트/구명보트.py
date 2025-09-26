"""
최대 2명

100kg -> 2번쨰 사람과 4번째 사람은 같이 탈 수 있다.

[50, 50, 70, 80]
일단 무거운 사람은 무조건 태우고 -> 가벼운 사람을 태웠을때 제한이 안넘어가면 태우고 -> 아니면 그대로 둠
투포인터!
"""

def solution(people, limit):
    answer = 0
    
    people.sort()
    left = 0
    right = len(people) - 1
    
    while (left <= right):
        if (people[left] + people[right] <= limit):
            left += 1
        right -= 1
        answer += 1
    
    return answer