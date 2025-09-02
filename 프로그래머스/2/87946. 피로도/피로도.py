"""
최소 필요 피로도 >= 소모 피로도

순열 개수 만큼 나온다. 

1) 1 2 3 -> 80이 60이 됨 -> 60이 20이 됨 -> 다음에 못함. 

순열을 만들어서 순열 개수만큼 한다. 

순열로 횟수를 만들어 -> 만약에 현재 k가 각 0번째보다 크거나 같으면 -> 계속해 그리고 횟수 +1 -> 작으면 -> 그 다음으로 바로 넘어가 -> 그리고 max 값을 반환해
"""
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for perm in permutations(dungeons):
        fatigue = k
        temp = 0
        for stage in perm:
            if (fatigue >= stage[0]):
                fatigue -= stage[1]
                temp += 1
            else:
                break
        answer = max(temp, answer)
        if answer == len(dungeons):
            return answer
            
    return answer