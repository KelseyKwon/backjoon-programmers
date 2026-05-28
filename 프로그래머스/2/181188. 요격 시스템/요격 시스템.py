"""
끝에가 더 작은것 나열

1, 4 4, 5 3, 7 4, 8

1부터 14까지
각 칸마다 몇개가 겹쳐져 있는지

4 직전에 쏘면 -> 하나만 
4 직전에 쏘면 -> 3개 다 가능!
 
"""

def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    cur_right = -1
    for left, right in targets:
        if left < cur_right:
            continue
        else:
            answer += 1
            cur_right = right
    
    return answer
            