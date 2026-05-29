"""
0 다이아 1 iron 2 stone

현재 상황에서 가장 최선의 선택을 해야 한다. -> 그리디!
순서는 상관 없다 -> 그리디!
"""

def solution(picks, minerals):
    answer = 0
    pick_num = sum(picks)
    if pick_num == 0:
        return 0
    
    info = []
    
    minerals = minerals[:pick_num * 5]
    for i in range(0, len(minerals), 5):
        chunked = minerals[i:i+5]
        
        dia = chunked.count("diamond")
        iron = chunked.count("iron")        
        stone = chunked.count("stone")   
        
        info.append((dia, iron, stone))
    
    info.sort(key=lambda x:(-x[0], -x[1], -x[2]))
    
    
    for i in info:
        dia, iron, stone = i
        if picks[0]:
            answer += dia + iron + stone
            picks[0] -= 1
        elif picks[1]:
            answer += dia * 5 + iron + stone
            picks[1] -= 1
        else:
            answer += dia * 25 + 5 * iron + stone
            picks[2] -= 1
    return answer
    
    