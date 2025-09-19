"""
installed 
1. 일단 stations의 숫자마다 좌, 우 w만큼 installed에 True
2. 그리고 각 N만큼 -> 만약에 x installed -> temp += 현재 index
그리고 count = 3이거나, installed = True이면 -> temp / w , 그리고 temp = 0으로 초기화
"""

# def solution(n, stations, w):
#     answer = 0

#     installed = [False for _ in range(n+1)]
    
#     for i in stations:
#         for j in range(i-w, i+w+1):
#             if (j >= 1 and j <= n):
#                 installed[j] = True
    
#     count = 0
#     for i in range(1, n+1):
#         if (count == 2*w+1 or installed[i] == True):
#             for j in range(i-w, i+w+1):
#                 if (j >= 1 and j <= n):
#                     installed[j] = True
#                     print("색칠함", j)
#                     count = 0
#             answer += 1
#         else:
#             print("아님" , i)
#             count += 1

#     return answer

"""
그럼 일단 빈칸을 찾아 -> 그리고 해당 빈칸의 길이를 2*w+1로 나누거의 ceil만큼 더해 answer에
"""
import math

def solution(n, stations, w):
    answer = 0
    
    length = 2*w+1
    prev = 1
    
    for i in stations:
        L = max(1, i-w)
        R = min(n, i+w)
        
        gap = L - prev
        if gap > 0:
            answer += math.ceil(gap / length)
        
        prev = R+1
    
    if prev <= n:
        answer += math.ceil((n-prev+1) / length)
    
    return answer