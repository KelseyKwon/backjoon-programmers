"""
number의 원소의 합은 10
각 단어의 길이는 12 이하.
discount : 14개 

discount의 인덱스 9 ~ len(discount) - 1 까지
잘라 그리고 각 배열마다 각 number의 원소들을 1식 줄여

그리고 모든 number의 원소가 0이 되면 해당 날짜를 반환해 (인덱스 + 1)
"""

"""
def solution(want, number, discount):
    answer = 0
    
    for i in range(9, len(discount)-1):
        temp_discount = discount[i-9:i+1]
        for k in temp_discount:
            for j in range(len(want)):
                if want[j] == k:
                    number[j]-=1
        # 모든 원소가 0인지 확인하는법
        if (all(x == 0 for x in number)):
            return i+1
    
    return 0
"""

"""
슬라이딩 윈도우!
Counter는 파이썬 collections모듈에 있는, 빈도수 세기 전용 딕셔너리
"""
from collections import Counter

def solution(want, number, discount):
    need = dict(zip(want, number))
    n = len(discount)
    
    # number의 합이 10이니까 discount의 원소의 길이 10이 안되면 조건 미충족
    if n < 10:
        return 0
    
    #초기 10일 빈도
    window_cnt = Counter(discount[:10])
    
    def ok():
        return all(window_cnt.get(item, 0) >= need[item] for item in need)
    
    answer = 1 if ok() else 0
    
    for i in range(10, n):
        out_item = discount[i-10]
        in_item = discount[i]
        
        # 윈도우에서 빠지는 항목
        window_cnt[out_item] -= 1
        if window_cnt[out_item] == 0:
            del window_cnt[out_item]
            
        #윈도우에 새로 들어오는 항목
        window_cnt[in_item] += 1
        
        if ok():
            answer += 1
            
    return answer