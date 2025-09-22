"""
귤을 크기별로 분류 -> 서로 다른 종류의 수를 최소화하고 싶다.

"""
from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    info = defaultdict(int)
    
    #dict 생성
    for i in tangerine:
        info[i] += 1
    # 딕셔너리는 .sort()의 메서드를 갖고 있지 않다.
    # info.sort(key= lambda x: info[x], reverse = True)
    counts = sorted(info.values(), reverse = True)
    
    # for key in info.keys():
    #     temp = info[key]
    #     if k >= temp:
    #         k -= temp
    #         answer += 1
    #         continue
    #     elif k>0 and k< emp:
    #         answer += 1
    #         break
    #     elif k == 0:
    #         break
    # 이렇게 세가지로 경우를 쪼개는 것보다 그냥 k > temp이면 무조건 1 더하고,
    # k <= temp이면 1더하고 break하는게 더 나음.
    for c in counts:
        if k > c:
            k -= c
            answer += 1
        else:
            answer += 1
            break
    return answer