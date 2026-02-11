"""
요격 미사일 최소 -> 모든 폭격 미사일을 요격!

# 폭격 미사일
A 나라 : x 축에 평행한 직선 형태, 개구간 (s, e) 형태로 표현됨
B 나라 : x 좌표에서 y축에 수평이 되도록 미사일 발사, x좌표에 걸쳐 있는 모든 폭격 미사일 관통

# 요격 미사일
실수인 x 좌표에서도 발사 가능 -> 즉, 중간에서도 발사 가능하다. 

      4 5
      4 5 6 7 8
                  10 11 12 13 14
                     11 12 13
        5 6 7 8 9 10 11 12
    3 4 5 6 7
1 2 3 4

그리디?? 

1번에 쏴 -> 3번에 쏴 -> 4번에 쏴 -> 5번에 뽜 -> 10번에 쏴 -> 11번에 쏴

1 3 4 5 10 11
2 3 4 5 10 11
3 4 5 10 11

일단 [0]을 기준으로 정렬 하고
[1, 4] [3, 7] [4, 5] [4, 8] [5, 12] [10, 14] [11, 13]

만약에 이전 배열의 max가 다음 구간에 속해있어 -> 그러면  4  5 12
3 < 4 < 7 -> x x
4 < 5 < 8 -> x x
10 < 12 < 14, 11 < 12 < 13 -> x x x
"""

def solution(targets):
    answer = 0
    N = len(targets)
    
    targets.sort(key=lambda x: x[1])
    
    cur_flag = -1
    # print(targets)
    for left, right in targets:
        # 속해있지 않으면 => visited = True, count + 1, flag 갱신 그 다음 
        if left >= cur_flag:
            answer += 1
            cur_flag = right
    return answer