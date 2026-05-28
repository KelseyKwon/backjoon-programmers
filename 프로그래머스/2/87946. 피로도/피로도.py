"""
모든 경우의 수를 다 따져 봐야 함.

"""

def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons) + 1)]
    
    def backtrack(cur_k, level):
        max_level = level
        if level == len(dungeons):
            return max_level
        
        for i, d in enumerate(dungeons):
            if not visited[i] and d[0] <= cur_k:
                visited[i] = True
                
                # 중요 ! 백트랙 -> 다음 단계로 넘어가고, 그 결과 중 가장 큰 값을 받아와서 갱신하기
                result = backtrack(cur_k - d[1], level+1)
                max_level = max(max_level, result)
                
                visited[i] = False
        return max_level
    
    return backtrack(k, 0)
    
    