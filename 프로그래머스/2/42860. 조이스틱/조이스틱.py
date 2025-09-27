"""
제일 큰것부터 하고 -> 거기서 그 다음 큰 대

가로 이동이랑 세로 이동을 독립적으로 생각하면 됨!
"""

def solution(name):

    answer = 0
    
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        # 좌우 변경은 계속 갱신된다. 
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    answer += min_move
    return answer