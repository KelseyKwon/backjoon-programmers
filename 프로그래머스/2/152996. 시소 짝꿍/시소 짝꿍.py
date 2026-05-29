from collections import Counter

def solution(weights):
    info = Counter(weights)
    answer = 0
    
    for w in info:
        if info[w] > 1:
            answer += info[w] * (info[w] - 1) // 2
            
        if w * 3 % 2 == 0 and w * 3 // 2 in info:
            answer += info[w] * info[w * 3 // 2]
            
        if w * 2 in info:
            answer += info[w] * info[w * 2]
            
        if w * 4 % 3 == 0 and w * 4 // 3 in info:
            answer += info[w] * info[w * 4 // 3]
            
    return answer