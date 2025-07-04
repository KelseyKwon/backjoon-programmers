def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boats = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람 태움
        # 무거운 사람은 무조건 태움
        right -= 1
        boats += 1
    return boats
