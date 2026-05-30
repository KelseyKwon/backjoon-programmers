"""
배달 및 수거를 하는거!

최대 cap만큼한 상자를 실을 수 있다.

n은 5! 
0에 위치...

최단 거리 -> bfs!

bfs((0, 1))

i) 그리고, cap<인 것까지만 배달해. 
ii) 그리고, 없애고, 4개를 실어.
"""

def solution(cap, n, deliveries, pickups):
    # 1. 어떻게 끝에서부터 cap 미만인 인덱스를 알 수 있냐?
    cur = 0
    turn = []
    for i in range(len(deliveries) - 1, -1, -1):
        if deliveries[i] == 0:
            continue
        else:
            cur_box = 0
            for j in range(i, -1, -1):
                if cur_box + deliveries[j] > cap:
                    break
                cur_box += deliveries[j]
                deliveries[j] = 0
            
            turn.append(i)
    
    return sum(turn) * 2 + 2*len(turn)
        
        