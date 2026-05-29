from itertools import combinations

def solution(n, q, ans):
    answer = 0
    nums = [i for i in range(1, n+1)]
    list_comb = list(combinations(nums, 5))
    
    for comb in list_comb:
        for i in range(len(q)):
            if len(set(q[i]) & set(comb))!=ans[i]:
                break
        else:
            answer += 1   
    
    return answer