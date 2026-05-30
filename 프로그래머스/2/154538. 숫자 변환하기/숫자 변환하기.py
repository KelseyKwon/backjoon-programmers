"""
최소 연산 횟수 = bfs!
"""
from collections import deque

def solution(x, y, n):
    q = deque([(x, 0)])
    visited = set([x])
    
    while q:
        cur_val, cnt = q.popleft()
        if cur_val == y:
            return cnt
        for next_val in [cur_val + n, cur_val * 2, cur_val * 3]:
            if next_val <= y and next_val not in visited:
                visited.add(next_val)
                q.append((next_val, cnt + 1))
            
    return -1