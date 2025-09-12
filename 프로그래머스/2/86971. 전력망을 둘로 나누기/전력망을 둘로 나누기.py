"""
n개, n-1 의 배열. (1 ~ 99번) 
그러면, N-1 x N-1 -> 99x99 -> 10000개 이하.
송전탑의 개수를 최대한 비슷하게 맞추기.

연결 -> linkedlist!


2 -> 3
3 -> 2, 4
4 -> 3, 5, 6, 7
5 -> 4
6 -> 4
7 -> 4, 8, 9
8 -> 7
9 -> 7

즉, 모든 wires마다 하나를 없애고, (하나를 통과하고, )

"""
from collections import defaultdict
import sys


def solution(n, wires):
    answer = sys.maxsize

    def dfs(start, graph, visited):
        """
        #여기서는 n번에서, 1번부터 차례대로  2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 이런식으로
        # 즉, 넣고, 그리고 방문하지 않았으면, 추가해.
        if start not in graph:
            return count
        
        for i in graph[start]:
            if not visited[i]:
                dfs(graph, i, count+1)
            
        return count
        """
        stack = [start]
        visited[start] = True
        cnt = 1
        while stack:
            v = stack.pop()
            for nv in graph[v]:
                if not visited[nv]:
                    visited[nv] = True
                    cnt += 1
                    stack.append(nv)
        return cnt
    
    for i in range(n-1):
        graph = defaultdict(list)
        visited = [False for _ in range(n+1)]
        for j in range(n-1):
            # i == j이면, linked list에 추가하는거 빼.
            if (i == j):
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False for _ in range(n+1)]
        
        a, b = wires[i]
        cnt = dfs(a, graph, visited)
        
        diff = abs(cnt - (n - cnt))
        answer = min(answer, diff)
    
    return answer
            
        # 그리고 이걸로 dfs 돌려. 
        
    
