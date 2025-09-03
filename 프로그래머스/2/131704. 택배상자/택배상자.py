"""
1 ~ n번까지 번호가 증가하는 순서대로 컨테이너 벨트에 일렬로 놓여 영재에게 전달됨.
현재 트럭에 실어야 하는 순서가 아니면 -> 다른 곳에 보관.
이용해도 원하는 순서대로 상자를 싣지 못하면, 더 이상 상자를 싣지 않음.

4, 3, 1, 2, 5
1, 2, 
4, 3, 

1, 2, 3, 4
5, 4, 3, 2, 1 일단 큐에 넣고, (큐를 두번 선언) 양쪽 다에 없으면 -> return 정답 배열
각각의 큐에서 뺴낼때마다 count 증가

큐는 크게 보조컨테이너 벨트, 없는거. 
그리고 answer list를 따로 선언해. 
"""

# from collections import deque

# def solution(order):
#     answer = 0
    
#     num = len(order)
    
#     # 큐 선언
#     # 일단 먼저 기존에 꺼 보고 -> 보조 컨테이너에서 맞으면 -> 
#     # 근데 다 안맞ㅇㅁ
#     sub_container = deque()
    
#     for i in range(1, num+1):
#         # 현재 있는 상자랑 order가 맞으면 answer에 넣고
#         if (i == order[i-1]):
#             answer += 1
        
#         # 보조 컨테이너랑 같으면
#         elif (sub_container and sub_container[0] == order[i-1]):
#             sub_container.popleft()
#             answer += 1
        
#     return answer

from collections import deque

def solution(order):
    q = deque([i for i in range(1, len(order) + 1)])
    stack = []
    count = 0
    
    for i in order:
        # 스택에 원하는 상자가 있으면 트럭에 바로 싣기
        if stack and stack[-1] == i:
            count += 1
            stack.pop()
        else:
            # 메인 벨트의 맨 앞이 원하는 상자가 될 때까지 하나씩 스택으로 옮기기
            while q and q[0] != i:
                stack.append(q.popleft())
            
            # 원하는 상자가 메인 벨트 맨 앞에 도착하면 꺼내서 트럭에 싫기
            if q and q[0] == i:
                count += 1
                q.popleft()
                
            #
            else:
                break
    return count