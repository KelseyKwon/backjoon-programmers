"""
만약에 폭격되지 않았어 -> 그러면 끝나기 직전에 쏘면 된다!

그리고, 그 숫자를 포함하고 있는 target들을 visited처리하면 됨.
"""

def solution(targets):
    result = 0
    
    targets.sort(key=lambda x: x[1])
    prev_target = -1
    
    for i in range(len(targets)):
        if prev_target <= targets[i][0]:
            result += 1
            prev_target = targets[i][1]
    return result
            