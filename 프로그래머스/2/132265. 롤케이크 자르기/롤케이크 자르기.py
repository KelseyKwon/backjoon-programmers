from collections import Counter

def solution(topping):
    answer = 0
    c = Counter(topping)
    new_top = set()
    
    for t in topping:
        new_top.add(t)
        c[t] -= 1
        
        if c[t] == 0:
            del c[t]
        
        if len(c) == len(new_top):
            answer += 1
    
    return answer