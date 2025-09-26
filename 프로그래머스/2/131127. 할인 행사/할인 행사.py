"""
제품 & 수량이 10일 연속ㅇ로 일치할 때.
sliding window! 
"""
from collections import defaultdict
from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    my_fruit = {}
    
    for fruit, i in zip(want, number):
        my_fruit[fruit] = i
    
    for i in range(len(discount) - 9):   
        discount_fruit = Counter(discount[i:i+10])
        # for k in my_fruit.keys():
        #     discount_fruit[k] -= my_fruit[k]
        # if (all(x == 0 for x in discount_fruit.values())):
        #     return i-9
        if discount_fruit == my_fruit:
            answer += 1
    return answer