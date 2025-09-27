"""
항상 "ICN" 공항에서 출발.
방문하는 공항 경로를 배열에 담아 return

항공권을 모두 사용해야 함.
2개 이상 -> 알파벳 순서가 앞서는 것 (알파벳 순서대로 정렬)
"""
from collections import defaultdict

def solution(tickets):
    answer = []
    
    info = defaultdict(list)
    
    for depart, dest in tickets:
        info[depart].append(dest)
    # 알파벳 순서대로 정렬
    for depart in info:
        info[depart].sort(reverse = True)
    
    stack = ["ICN"]
    route = []
    while stack:
        cur = stack[-1]
        if info[cur]:
            stack.append(info[cur].pop())
        else:
            route.append(stack.pop())
            
    
    return route[::-1]