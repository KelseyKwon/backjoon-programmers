"""
i에서 j로 가는 길이가 양수인 경로가 있는지 없는지

중간 노드를 찍어서 갈 수 있으면 -> ok.
"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
matrix = [[0]*n for _ in range(n)]

def bfs(start):
    q = deque([start])
    visited = [0]*n
    while q:
        v = q.popleft()
        for i in range(n):
            if not visited[i] and graph[v][i] == 1:
                visited[i] = 1
                matrix[start][i] = 1
                q.append(i)

for i in range(n):
    bfs(i)

# ← 이 부분이 빠져 있었음
for row in matrix:
    print(*row)
