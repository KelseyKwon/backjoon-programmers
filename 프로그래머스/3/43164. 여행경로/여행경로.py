"""
공항 수는 3<= <=10000
[a, b] means a -> b exists

linked_list 사용해서 dfs!

ICN -> JFK
HND -> IAD
JFK -> HND

--> ICN -> JFK -> HND -> IAD

ICN -> SFO
ICN -> ATL
SFO -> ATL
ATL -> ICN
ATL -> SFO

ICN : SFO, ATL -> 정렬해 ICN -> ATL -> ICN -> SFO -> ATL -> SFO

이차원 배열을 선언해서 -> 인접리스트형식으로 만들기.

1) 인접리스트 (이차원배열)
2) dfs -> ICN부터 시작 -> 만약에 티켓을 사용하지 않았고, 각 배열의 첫번쨰 도시부터 돌아
3) 그리고 없으면 빠져나와서 다음 큐부터
"""
from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for depart, destination in tickets:
        graph[depart].append(destination)
    
    for k in graph:
        graph[k].sort(reverse=True)
        
    route = []
    stack = ["ICN"]
    
    # stack에 값이 있는 동안
    while stack:
        cur = stack[-1]
        # 아직 방문하지 않았다면
        if graph[cur]:
            stack.append(graph[cur].pop())
        # 방문 했으면
        else:
            route.append(stack.pop())
        
    
    return route[::-1]