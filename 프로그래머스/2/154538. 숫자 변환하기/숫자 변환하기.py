"""
x + n
x * 2
x * 3
최소 연산 횟수...
"""
from collections import deque

def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    visited = set([x])
    
    while q:
        cur_num, cnt = q.popleft()
        if cur_num == y:
            return cnt
    
        for next_num in [cur_num + n, cur_num * 2, cur_num * 3]:
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cnt + 1))
    
    return -1
        
        