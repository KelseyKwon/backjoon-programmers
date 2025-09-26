"""
서로 다른 종류의 귤의 개수가 최소가 되어야 함.

1 : 1
2 : 2
3 : 2
4 : 1
5 : 2

values을 기준으로 정렬 (내림차순으로) -> k-= 
"""
from collections import Counter

def solution(k, tangerine):
    count = 0
    
    info = Counter(tangerine)
    sort_info = sorted(info.values(), reverse = True)
    
    for i in sort_info:
        if (k - i) > 0:
            k -= i
            count += 1
        else:
            return count + 1
    
    return count