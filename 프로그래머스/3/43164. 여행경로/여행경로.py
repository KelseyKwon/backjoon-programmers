from collections import defaultdict

def solution(tickets):
    answer = []
    # 1. 초기화
    linked_list = defaultdict(list)
    cities = set()
    
    for rows in tickets:
        linked_list[rows[0]].append(rows[1])
    
    # 2. 알파벳으로 정렬
    for k in linked_list.keys():
        linked_list[k].sort(reverse = True)
        
    stack = ["ICN"]
    while stack:
        s = stack[-1]
        if not linked_list[s]:
            answer.append(stack.pop())
        else:
            stack.append(linked_list[s].pop())
    return answer[::-1]
    
    
    
    
    return answer