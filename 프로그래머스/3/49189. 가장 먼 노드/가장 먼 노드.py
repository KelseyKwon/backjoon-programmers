from collections import defaultdict
from collections import deque
import sys

def solution(n, edge):
    # MAX = sys.maxsize
    # answer = 0
    
    info = defaultdict(list)
    # result = [MAX for i in range(n+1)]
    
    for u, v in edge:
        info[u].append(v)
        info[v].append(u)
    
    # q = deque()
    # result[0] = 0
    # result[1] = 0
    dist = [-1] * (n+1)
    dist[1] = 0
    
    q = deque([1])
    
    # for i in info[1]:
    #     q.append((i, 1))
    while q:
        # n_node, count = q.popleft()
        # result[n_node] = min(count, result[n_node])
        # for k in info[n_node]:
        #     q.append((k, count + 1))
        u = q.popleft()
        for v in info[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    
    # sum(1 if k == max(result) else 0 for k in result)
    maxd = max(dist[1:])
    answer = sum(d == maxd for d in dist[1:])
        
    return answer