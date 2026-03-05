"""
항상 같은 위치에 공을 놓고 쳐서 -> 담긴 위치에 노힌 공을 맞춘다.
최소 얼마의 거리를 굴러가야 하는지

m, n 길이 (1000 이하, 3이상)
startX, startY : 공의 처음 위치
balls -> 공 위치 배열
3, 2 -> 9 4 
3, 1.5 -> 9 2.25 11.25

case1) 즉, y좌표가 같으면 항상 위에 맞춰야됨. x좌표가 같으면 항상 옆에 맞춰야됨.
case2) 나랑 똑같을때 -> 그냥 꼭짓점과의 거리가 최소인 데를 하면 됨.
case3) 둘다 다를때 -> 그냥 위, 왼쪽

-3, 7 7, 3 -> 116
13, 3 3, 7 -> 116

"""

def solution(m, n, startX, startY, balls):
    answer = []
    
#     def upperCase(endX):
#         # y좌표를 0에서 뺴서 두배한거랑, n에서 뺴서 2배한거
#         return (min(startY, n - startY) * 2) ** 2 + (startX - endX) ** 2
    
#     def leftCase(endY):
#         return (min(startX, n - startX) * 2) ** 2 + (startY - endY) ** 2
    
#     def sameCase():
#         # 0, 0 0, 10 10, 0 10, 10
#         # ^2 ^2 ^2 abs
#         return min((startX ** 2 + startY ** 2),
#                    ((m-startX) ** 2 + startY ** 2),
#                    (startX ** 2 + (n-startY) ** 2),
#                    ((m-startX) ** 2 + (n-startY) ** 2)
#                    )
    
    for endX, endY in balls:
        # cur_dist = 0
        candidates = []
        
        # 왼 -> 위 -> 오 -> 아
        # end가 목표공!
        
        # 목표 공이 왼쪽에 있을때
        if not (startX > endX and startY == endY):
            candidates.append((startX + endX) ** 2 + (startY - endY) ** 2)
        if not (startX == endX and startY < endY):
            candidates.append((startX - endX) ** 2 + (2*n - startY - endY) ** 2)
        if not (startX < endX and startY == endY):
            candidates.append((2*m - startX - endX) ** 2 + (startY - endY) ** 2)
        if not (startX == endX and startY > endY):
            candidates.append((startX - endX) ** 2 + (startY + endY) ** 2)
        answer.append(min(candidates))
            
    return answer