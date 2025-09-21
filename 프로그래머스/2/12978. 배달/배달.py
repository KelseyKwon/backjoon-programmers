"""
1 이상 50 이하. 
"""
import heapq

def solution(N, road, K):
    # 각 노드에 연결된 간선들을 저장할 리스트
    graph = [[] for _ in range(N+1)]
    
    #출발점에서 각 노드까지의 최단 거리
    distances = [float("inf")] * (N+1)
    distances[1] = 0
    
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    heap = []
    
    # 우선순위 큐 : (현재까지의 거리, 노드)
    heapq.heappush(heap, (0, 1))
    while heap:
        dist, node = heapq.heappop(heap)
        
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
    
    return sum(1 for dist in distances if dist <= K)