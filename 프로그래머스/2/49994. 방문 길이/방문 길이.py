"""
중복 방지 -> set!
set에 좌표를 담아 -> (시작, 끝) / (끝, 시작) 으로 

예외 처리 : 범위 안에 있고, 그리고 set / 2을 반환해.
"""

def inRange(x, y):
    return -5 <= x <= 5 and -5 <= y <= 5

def solution(dirs):
    cur_x, cur_y = 0, 0
    answers = set()
    
    moves = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}
    
    for d in dirs:
        dx, dy = moves[d]
        nx, ny = cur_x + dx, cur_y + dy
        if inRange(nx, ny):
            answers.add(((cur_x, cur_y), (nx, ny)))
            answers.add(((nx, ny), (cur_x, cur_y)))
            cur_x, cur_y = nx, ny
        
    
    return len(answers)//2