"""
전체를 다 봐야돼! -> 백트래킹??

"""

def solution(k, dungeons):
    answer = 0
    lens = len(dungeons)
    visited = [False] * lens
    
    def backtrack(fatigue, count):
        nonlocal answer
        answer = max(count, answer)
        for d in range(lens):
            if not visited[d] and dungeons[d][0] <= fatigue:
                visited[d] = True
                backtrack(fatigue - dungeons[d][1], count+1)
                visited[d] = False
                
    backtrack(k, 0)
    return answer