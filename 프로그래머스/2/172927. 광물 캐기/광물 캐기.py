"""
사용할 수 없을 때까지 사용 (즉, 5번을 꼭 사용해야 함)
주어진 순서대로만 캘 수 있다.
end 조건 : 모든 광물을 캐거나, 더 사용할 곡괭이가 없을때까지

dia, iron, stone 순으로 되어 있음...

cur_turn = 0
+1 해. 그리고, cur_turn = 5이면, 그 다음으로 넘어가

max_cur_turn = picks[i] * 5
cur_turn = max_cur_turn -> 인덱스 하나 증가시켜
"""

def solution(picks, minerals):
    answer = 0
    N = len(minerals)
    info = []
    
    able_pick = sum(picks) * 5
    minerals = minerals[:able_pick]
    # print(minerals)
    
    # print(info)
    for i in range(0, N, 5):
        # diamond_nums = sum(mins == 'diamond' for mins in minerals[i:min(i+5, N)])
        diamond_nums = minerals[i:min(i+5, N)].count('diamond')
        iron_nums = minerals[i:min(i+5, N)].count('iron')
        stone_nums = minerals[i:min(i+5, N)].count('stone')
        info.append([diamond_nums, iron_nums, stone_nums])
    # 다이아 개수를 기준으로 정렬
    info.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    print(info)
    
    # 0은 다이아 곡괭이, 1은 철 곡괭이
    fatigue = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    cur_kok = 0
    
    # i[0] i[1] i[2] 가 각각 다이아, 철, 돌
    for i in info:
        # 모두 다 0이면 문제가 됨 -> 왜냐? 연속적으로 0일 수 있으므로
        
        # 1, 3, 2 별로 돈다. 
        # if picks[cur_kok] == 0:
        #     if cur_kok == 2:
        #         break
        #     cur_kok += 1
        while cur_kok < 3 and picks[cur_kok] == 0:
            cur_kok += 1
        if cur_kok == 3:
            break
        dia_fatigue = i[0] * fatigue[cur_kok][0]
        iron_fatigue = i[1] * fatigue[cur_kok][1]
        stone_fatigue = i[2] * fatigue[cur_kok][2]
        
        picks[cur_kok] -= 1
        answer += dia_fatigue + iron_fatigue + stone_fatigue
    
    return answer