"""
"headgear" : "yellow_hat", "green_turban"
"eyewear" : "blue_sunglasses"

이러면 
1 : 3가지
2 : 2

1 : 5가지
2 : 얼굴부터 -> 얼굴 * 상의 + 얼굴 * 하의 + 얼굴 * 겉옷
3 : (얼굴, 상의) 조합 + 하의, (얼굴, )
4 : (얼굴 , 상의, 하의) + 겉옷, (얼굴, 상의, 겉옷) 

순열 조합 -> permutations.
key들을 갖는 배열이랑 각 key & value를 갖는 dict 선언
그리고 permutation당, 각 키에 해당되는 배열의 킬이 만큼 곱해. 
"""

"""
시간 초과 풀이
from itertools import combinations
from collections import defaultdict

def solution(clothes):
    answer = 0
    keys = set()
    info = defaultdict(list)
    
    # keys = [headgear, eyewear]
    # 2, 1이야 그러면 1, 2, 2
    #2, 3이야 그러면 1, 2, 6
    # info = {"headgear" : ["yellow_hat", "green_turban"]}
    
    for i in range(len(clothes)):
        keys.add(clothes[i][1])
        info[clothes[i][1]].append(clothes[i][0])
    
    for name, kind in clothes:
        keys.add(kind)
        info[kind].append(name)
    
    for i in range(1, len(keys)+1):
        # 이러면 headgear / eyewear / headgear, eyewear
        
        cur_pick = combinations(keys, i)
        print(cur_pick)
        
        for cur_pick in combinations(keys, i):
            cur_answer = 1
            for k in cur_pick:
                cur_answer *= len(info[k])
            answer += cur_answer
            
    return answer
"""
def solution(clothes):
    kinds = {}
    for name, kind in clothes:
        kinds[kind] = kinds.get(kind, 0) + 1  # get으로 초기값 0 처리

    answer = 1
    for cnt in kinds.values():
        answer *= (cnt + 1)
    return answer - 1