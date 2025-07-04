"""
앞에서부터 막을 수 있는 최대 라운드의 개수
-> 그러면 x라운드까지 막을 수 있는가? 라는 결정 문제로 바꾸고, 이진탐색으로 바꾼다!

low = 1, high = len(enemy)
mid = (low + high) // 2
앞에서 mid 개 라운드를 막을 수 있는지 확인 -> 가장 큰 k개 공격은 무적권으로 막고. 나머지는 병사로 막았을때, 가능하다면 -> 더 많이 막을 수 있는지 탐색. 불가능하다면 -> 줄여야 한다.

1. k >= len(enemy)
2. 
"""
def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    left, right = 1, len(enemy)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        temp = sorted(enemy[:mid], reverse=True)  # 내림차순 정렬
        need = sum(temp[k:])  # 무적권 k개 사용하고 나머지 병사 필요량
        
        if n >= need:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
