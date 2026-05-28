"""
만약에 2번이 열리면
1, 5, 2 
2, 9, 2

최대 -> 6번!

dfs?

그래프 구성, 확산, 최적의 순서를 각각 다르게 적용해야 한다!
"""
from collections import deque

def solution(n, infection, edges, k):
    graph = [[] for _ in range(n+1)]
    for u, v, pipe_type in edges:
        graph[u].append((v, pipe_type))
        graph[v].append((u, pipe_type))
        
    # 확산
    def spread(current_infected, target_pipe):
        infected = set(current_infected)
        queue = deque(current_infected)
        
        while queue:
            cur_n = queue.popleft()
            for neighbor, pipe_type in graph[cur_n]:
                if pipe_type == target_pipe and neighbor not in infected:
                    infected.add(neighbor)
                    queue.append(neighbor)
        return infected
    
    # 최적의 경로 찾기
    # 왜 이렇게 하냐? -> 현재 내가 어떤 상황에 있는지를 다음 단계로 전달하는 수단이기 때문에.
    # 초기 설정값을 설정한 이유 -> 최소한 지금 확보한 것은 보장받기 위해!
    def dfs(current_infected, remaining_k):
        if remaining_k == 0:
            return len(current_infected)
        max_infected = len(current_infected)
        for pipe_type in [1, 2, 3]:
            next_infected = spread(current_infected, pipe_type)
            result = dfs(next_infected, remaining_k - 1)
            max_infected = max(max_infected, result)
        return max_infected
        
    initial_infected = {infection}
    return dfs(initial_infected, k)