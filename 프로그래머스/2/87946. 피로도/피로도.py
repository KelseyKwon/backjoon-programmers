"""
유망함수 : 방문하지 않았고, 최소 필요 피로도보다 크거나 같다. 
"""

def solution(k, dungeons):
    answer = -1
    visited = [False] * len(dungeons)
    
    def backtrack(cur_k, cnt, visited):
        answer_max = cnt
        for i in range(len(dungeons)):
            if (cur_k >= dungeons[i][0] and not visited[i]):
                visited[i] = True
                answer_max = max(
                    answer_max, backtrack(cur_k - dungeons[i][1], cnt+1, visited)
                )
                visited[i] = False
        return answer_max
    
    max_answer = backtrack(k, 0, visited)
    return max_answer