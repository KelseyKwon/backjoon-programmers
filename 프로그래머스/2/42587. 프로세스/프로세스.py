"""
queue.popleft() -> 만약 큐에 우선순위가 더 높은 프로세스가 있으면 -> 다시 큐에 넣기.
아니면 -> 실행. 

인덱스 : 2
0 : 2
1 : 1
2 : 3
3 : 2


"""
from collections import deque
from collections import defaultdict

def solution(priorities, location):
    answer = 0
    info = defaultdict(int)
    
    q = deque([i for i in range(len(priorities))]) #[0, 1, 2, 3]
    for index, value in enumerate(priorities):
        info[index] = value # 0 : 2, 1 : 1, 
    while q:
        cur_index = q.popleft()
        
        for k in q:
            if info[k] > info[cur_index]:
                q.append(cur_index)
                break
        else:
            answer += 1
            if (cur_index == location):
                return answer