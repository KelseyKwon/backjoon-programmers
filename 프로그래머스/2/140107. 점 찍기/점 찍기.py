"""
0부터 d까지 돌면서. 

0,0 0,2 0,4 2,0 2,2 4,0 

x좌표부터 시작 -> d까지

"""
import math

def solution(k, d):
    answer = 0
    
#     for i in range(0, d+1, k):
#         can_y = int (math.sqrt(d*d - i*i))
#         answer += (can_y // k) + 1
#         if (can_y + 1) ** 2 + i ** 2 <= d ** 2:
#             answer += (can_y + 2)
#         else:
#             answer += (can_y + 1)
    
#     return answer

    for i in range(0, d+1, k):
        can_y = int (math.sqrt(d*d - i*i))
        answer += (can_y // k) + 1 # 경계값까지 생각하기
    
    return answer