"""
1부터 n까지 있는 정수 배열.
ans -> 각각 q[n]에 일치한 정수의 개수를 리턴. 

조합을 하고 -> 5개, 1 ~ 10까지, 조합 5개 10C5 = 그 중에 1 2 3 4 5 -> 여기서 ans[n]개 이상 틀리면
-> x.

그러면 n개 이상 다른거
"""
from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    n_list = [i for i in range(1, n+1)]
    list_comb = list(combinations(n_list, 5))
    N = len(q)
    
    # [1, 2, 3, 4, 5]
    for combs in list_comb:
        # [1, 2, 3, 4, 5]
        for i in range(N):
            # 아래와 같이 하면 순서도, 숫자도 같아야 한다... 그래서 순서가 없는 set으로 해야함!
            # if (sum(1 for a, b in zip(combs, q[i]) if a != b) != ans[i]):
            sums = len(set(combs) & set(q[i]))
            if sums != ans[i]:
                break
        # 만약에 break에 걸리지 않으면
        else:
            answer += 1
        
            
    
    return answer