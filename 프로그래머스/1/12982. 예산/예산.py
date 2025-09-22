"""
최대한 많은 부서의 물품

1) 만약에 sum(d)가 <= budget : return len(d)
2) else : d.sort() -> [1, 2, 3, 4, 5] -> 가장 작은것부터 더해
3) 1 -> 2-> 3 -> 4(x) -> 넘으면 break, count을 반환해.
"""

def solution(d, budget):
    answer = 0
    
    if sum(d) <= budget:
        return len(d)
    else:
        d.sort()
        count = 0
        amount = 0
        for i in d:
            if (amount + i <= budget):
                amount += i
                count += 1
            else:
                return count