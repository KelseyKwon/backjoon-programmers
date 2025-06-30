import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(cur, target, visited, count):
    if cur == target:
        return count
    # 직계 관계(1촌)도 처리
    if target in relation[cur]:
        return count + 1

    for nxt in relation[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            res = dfs(nxt, target, visited, count + 1)
            # None이 아니면 찾은 것(0 이상의 정수)이므로 즉시 반환
            if res is not None:
                return res
    # 이 서브트리에서는 못 찾았음을 알리기 위해 None 반환
    return None

n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [False] * (n + 1)
relation = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    # 양방향 연결
    relation[u].append(v)
    relation[v].append(u)

visited[a] = True
result = dfs(a, b, visited, 0)

# 최종 결과: None이면 -1, 아니면 촌수
print(result if result is not None else -1)


