from collections import deque

def solution(priorities, location):
    count = 0
    q = deque()
    for index, v in enumerate(priorities):
        q.append((v, index)) # (2, 0), (1, 1) , (3, 2) 이렇게
        print(q)
    
    while q:
        cur_priority , index = q.popleft()
        if any(k[0] > cur_priority for k in q):
            q.append((cur_priority, index))
        else:
            count += 1
            if index == location:
                return count