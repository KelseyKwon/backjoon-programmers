"""
토핑이 중요!
동일한 가짓수의 토핑

0 ~ 3 3~ 마지막

토핑이 동일하게 하는 법!

모든 경우의수를 봐야 함
백트래킹??
"""
from collections import Counter

def solution(topping):
    set_dict = Counter(topping)
    answer = 0
    set_top = set()
    
    for i in topping:
        set_dict[i] -= 1
        set_top.add(i)
        if set_dict[i] == 0:
            set_dict.pop(i)
        
        if len(set_top) == len(set_dict):
            answer += 1
    return answer
    
    
        
    