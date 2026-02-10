"""
실행 대기 queue에서 대기중인 프로세스 하나 꺼냄
1. 우선순위
2. 꺼낸 순서

프로세스의 뒤에서부터 꺼낸다. 

프로세스의 뒤에서

0, 1, 2, 3
-> 3을 꺼내 -> 2부터 -> 2, 3, 0, 1

[2 1 3 2]
 0 1 2 3
 3 4 1.2
 
 3 2 2 1
 2 3 0 1
 
 1. priorities, 2. index
 
 그럼 3은 첫번쨰에 정해짐...
 

2야 -> 더 작은게 있어?

1032

1 1 9 1 1 1
0 1 2 3 4 5

6  5  1. 4  3 2

이렇게 하면 우선순위가 같은 프로세스들끼리의 처리 순서를 큐의 규칙대로 반영할 수 없다. -> 문제에 큐를 사용하라고 했으니까 그냥 큐를 사용하라!

따라서, 그냥 queue에 넣고, 만약에 현재 큐에 있는 것 중에서 하나라도 우선순위가 높다면,
다시 뒤로 append한다. 
없으면, 실행 -> answer += 1
"""
from collections import deque
def solution(priorities, location):
    answer = 0
    
    # indexed_priorities = [(i, val) for i, val in enumerate(priorities)]
    # indexed_priorities.sort(key=lambda x: (-x[1], -x[0]))
    # return indexed_priorities.index((location, priorities[location])) + 1
    
    q = deque([(i, value) for i, value in enumerate(priorities)])
    
    while q:
        cur = q.popleft()
        
        if any(cur[1] < other[1] for other in q):
            # 우선순위가 하나라도 높은게 있다면, 뒤로 빼기
            q.append(cur)
        else:
            answer += 1
            if (cur[0] == location):
                return answer
    