"""
최단경로로 이동했을 때 간선의 개수가 가장 많은 노드를 의미 = 가장 떨어진 노드

노드 개수 n, 간선에 대한 정보가 담긴 2차원 배열
양방향

linked_list -> dict을 통해서

1 : 2, 3
2 : 1, 3, 4, 5
3 : 1, 2, 4, 6
4 : 2, 3
5 : 2
6 : 3

이렇게 저장하고 -> 2번 부터 -> n번 노드까지 ->
세지 않은 노드면 : 시작 -> 결과를 answers 배열에 저장
그리고 min(answers)을 return


어떻게 최단 거리를 계산?
1번의 배열부터 -> 
만약 도착 노드와 같으면 -> return (즉, in을 써서 있음을 확인하면)
만약 방문하지 않았으면 -> dfs(해당 노드))
"""
# from collections import defaultdict

# def solution(n, edge):
#     answers = []
#     info = defaultdict(list)
    
#     def dfs(cur, dest, cost):
#         visited = [False] * (n+1)
#         if dest in info[cur]:
#             return cost
#         else:
#             for next in info[cur]:
#                 if not visited[next]:
#                     dfs(next, edge, cost+1)
            
    
#     for start, end in edge:
#         info[start].append(end)
#         info[end].append(start)
        
#     #2번부터 n번노드까지
#     for i in range(2, n):
#         answers.append(dfs(1, i, 1))
    
#     max_d = max(answers[1:])
#     return answers[1:].count(max_d)
    
#     return answer

from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    dist = [-1] * (n+1)
    dist[1] = 0
    
    q = deque([1])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    
    max_d = max(dist[1:])
    return dist[1:].count(max_d)