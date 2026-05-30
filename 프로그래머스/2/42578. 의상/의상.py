"""
종류별로 한가지식만.
총 개수와, 조합이 맞아야 함!
최소 1개 이상은 입어야 한다.

의상의 이름, 종류

(2 * 2 * 2 * 2 - 1) 

"""
from collections import defaultdict

def solution(clothes):
    info = defaultdict(int)
    for cloth in clothes:
        a, b = cloth
        info[b] += 1
    
    answer = 1
    for count in info.values():
        answer *= (count+1)
    return answer - 1