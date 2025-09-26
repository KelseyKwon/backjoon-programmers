"""
한번은 만나도록

"""

def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x: x[1])
    ok = [False] * len(routes)
    
    for i in range(len(routes)):
        if not ok[i]:
            camera = routes[i][1]
            ok[i] = True
            answer += 1
        for j in range(i+1, len(routes)):
            if camera >= routes[j][0] and camera <= routes[j][1] and not ok[j]:
                ok[j] = True
    
    return answer