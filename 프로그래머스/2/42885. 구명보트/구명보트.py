"""
50, 70, 80
50, 50, 70, 80

일단 무거운 사람 태워 -> 만약에 첫번째 태울 수 있으면 -> okey!

"""
from collections import deque
def solution(people, limit):
    people.sort()
    q = deque(people)
    count = 0
    
    while q:
        right = q.pop()
        if q and (right + q[0] <= limit):
            q.popleft()
        count += 1
    return count
        