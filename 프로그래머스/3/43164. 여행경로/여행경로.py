"""
항상 ICN공항에서 출발.
주어진 항공권을 모두 사용해야 함.
알파벳 순서대로 정렬하기
"""
from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for depart, dest in tickets:
        graph[depart].append(dest)
        
    for key in graph:
        graph[key].sort(reverse = True)
        
    stack = ["ICN"]
    route = []
    
    while stack:
        cur = stack[-1]
        if (graph[cur]):
            stack.append(graph[cur].pop())
        else:
            route.append(stack.pop())
    
    return route[::-1]