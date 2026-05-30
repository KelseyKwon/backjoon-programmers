from collections import Counter

def solution(topping):
    answer = 0
    
    top = Counter(topping)
    new_top = set()
    
    for t in topping:
        new_top.add(t)
        top[t] -= 1
        
        if top[t] == 0:
            del top[t]
        
        if len(top) == len(new_top):
            answer += 1
    return answer