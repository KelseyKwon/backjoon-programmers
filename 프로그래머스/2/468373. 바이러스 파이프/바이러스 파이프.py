"""
A, B, C를 최대한 k번 반복해서 열 수 있어.
infection부터 시작해서, edges를 다 열거야.

x, y, type

1 : (2, 1), (3, 1), (4, 3), (5, 2)
2 : (1, 1), (8, 3), (9, 2)
3 : 
...
10

그러면 초기에 감염된 것들을 넣고 -> 거기 stack과 연결된 것들, 파이프가 동일한것만
추가?
"""
from collections import deque
from collections import defaultdict


def solution(n, infection, edges, k):
    info = defaultdict(list)
    
    for e in edges:
        x, y, n = e
        info[x].append((y, n))
        info[y].append((x, n))
        
    def spread(infect, types):
        new_infect = set(infect)
        q = deque(infect)
        
        while q:
            cur_n = q.popleft()
            for neighbor, pipe_type in info[cur_n]:
                if pipe_type == types and neighbor not in new_infect:
                    new_infect.add(neighbor)
                    q.append(neighbor)
        return new_infect
    
    def dfs(cur_infected, rem_k):
        if rem_k == 0:
            return len(cur_infected)
        
        max_infected = len(cur_infected)
        
        
        for i in [1, 2, 3]:
            next_infected = spread(cur_infected, i)
            if len(next_infected) > len(cur_infected):
                result = dfs(next_infected, rem_k - 1)
                max_infected = max(max_infected, result)
        
        return max_infected
    
    infected = [infection]
    return dfs(set(infected), k)
    
    
    