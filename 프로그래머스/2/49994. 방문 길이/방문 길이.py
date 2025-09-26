"""

"""

def solution(dirs):
    answer = 0
    candidate = set()
    x, y = 0, 0
    direction = {"U" : [0, 1], "D" : [0, -1], "L" : [-1, 0], "R" : [1, 0]}
    
    def inRange(x, y):
        return -5<=x<=5 and -5<=y<=5
    
    for k in dirs:
        nx = x + direction[k][0]
        ny = y + direction[k][1]
        
        if (inRange(nx, ny)):
            candidate.add((x, y, nx, ny))
            candidate.add((nx, ny, x, y))
        
            x , y = nx, ny
    return len(candidate) // 2