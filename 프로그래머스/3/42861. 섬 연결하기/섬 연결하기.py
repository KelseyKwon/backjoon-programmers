"""
costs를 각 행의 3번째 원소를 기준으로 나열해.

그리고 가장 작은거부터 넣어 -> 0, 1
if len(set[0, 1]) = 4 -> 나와.
return 4. 

def solution(n, costs):
    answer = 0
    
    # 각 행의 3번째 값을 기준으로 정렬하는법
    costs.sort(key= lambda i: i[2])
    possible = set()
    
    for info in costs:
        start, end, cost = info[0], info[1], info[2]
        # 다 연결 가능하면 answer을 반환
        if len(possible) == n:
            return answer
        # 둘다 안에 있으면 추가하지마.
        elif start in possible and end in possible:
            continue
        possible.update({start, end})
        answer += cost
        
    
    return answer
"""
def solution(n, costs):
    costs = sorted(costs, key=lambda x:x[2])
    
    # 부모 배열 초기화 -> 각 정점이 자기 자신의 대표
    parents = [i for i in range(n)]
    
    # 부모를 찾는 함수.
    def find(parents, x):
        # 부모가 자기 자신이 아니라면, 더 위에 대표를 찾아 올라간다. 
        if parents[x] != x:
            parents[x] = find(parents, parents[x])
        # x의 대표 반환.
        return parents[x]
    
    # union : x, y가 속한 집합을 합치기
    def union(parents, x, y):
        x = find(parents, x)
        y = find(parents, y)
        
        # 더 작은 대표를 전체 대표로 삼기!
        if x < y:
            parents[y] = x
        else:
            parents[x] = y
            
    answer = 0
    for a, b, cost in costs:
        if find(parents, a) != find(parents, b):
            answer += cost
            union(parents, a, b)
    return answer
    