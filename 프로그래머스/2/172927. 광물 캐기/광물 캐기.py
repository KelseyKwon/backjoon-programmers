"""
5개 연속으로 캐니까 순서는 상관 없잖아
그니까 5개 기준으로 해서 -> dia, iron, stone의 개수가 많은 순서대로 나열해

단 마지막은 무조건 마지막
"""

def solution(picks, minerals):
    answer = 0
    pick_sum = sum(picks)
    info = []
    
    minerals = minerals[:5 * pick_sum]
    
    for i in range(0, len(minerals), 5):
        cur_min = minerals[i:i+5]
        dia = cur_min.count("diamond")
        iron = cur_min.count("iron")
        stone = cur_min.count("stone")
        
        info.append((dia, iron, stone))
    
    info.sort(key = lambda x : (-x[0], -x[1], -x[2]))
    
    for i in info:
        dia, iron, stone = i
        if picks[0]:
            picks[0] -= 1
            answer += dia + iron + stone
        elif picks[1]:
            picks[1] -= 1
            answer += dia * 5 + iron + stone
        else:
            picks[2] -= 1
            answer += dia * 25 + iron * 5 + stone
    
    return answer
            
            
    
    
    
        