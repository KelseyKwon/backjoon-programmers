"""
토핑의 개수에 따라 롤케이스 개수의 형평성이 결정된다!
숫자가 토핑이 종류를 의미 -> 이 토핑이 많아질수록!!
공평하게 나누는 경우의수를 구하기

투포인터?? -> 
left, right = 0, 0... 
"""

# def solution(topping):
#     answer = 0
#     # 길이가 1이면 -> 0
#     n = len(topping)
#     if (n == 1):
#         return 0
    
#     start = 0
#     # 만약에 왼쪽게 종류가 더 많아 -> start을 -1하기
#     # 오른쪽게 종류가 더 많아 -> start을 +1 하기
#     while start < n:
#         #왼쪽게 종류가 많아
#         left_num = len(set(topping[0:start+1]))
#         right_num = len(set(topping[start+1:n]))
        
#         if (left_num == right_num):
#             answer += 1
        
#         if (left_num > right_num):
#             start -= 1
#         else:
#             start += 1
    
#     return answer

from collections import Counter

def solution(topping):
    # topping의 원소 개수를 구해서 dictionary로 저장
    dic = Counter(topping)
    set_dic = set()
    answer = 0
    # topping에 있는 토핑마다
    for i in topping:
        #Counter에 있는 토핑의 개수를 빼기
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        # dictionary의 길이를 구하면 그냥 key 원소의 길이를 구한다.
        if len(dic) == len(set_dic):
            answer += 1
    return answer
        
        
        
    
    
    