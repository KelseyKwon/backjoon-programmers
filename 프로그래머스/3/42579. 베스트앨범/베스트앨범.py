"""
속한 노래가 많이 재생된 장르 먼저 수록
장르 내에서 많이 재생된 노래 먼저 수록 -> 같으면 고유 번호가 낮은 노래 먼저 수록

인덱스가 고유번호!
classic ; 1450회

1) 장르별로 재생된 횟수 더하기
2) 장르에 속한 고유번호이면 -> 해당 고유번호에서 재생횟수를 기준으로 정렬

장르의 종류는 100개 미만.

장르에 속한 곡이 하나라면 하나의 곡만 선택.

{"classic" : [500, 150, 800] , "pop" : [600, 2500]}

다 더하고 더한게 큰 것부터 -> 정렬하고 -> 상위 2개만 추출
"""

from collections import defaultdict

def solution(genres, plays):
    answer = []
    total = {}
    gen = {}
    
    for i in range(len(genres)):
        # "classic" :1450, "pop" : 3100 각 장르별 총 재생횟수
        total[genres[i]] = total.get(genres[i], 0) + plays[i]
        # {"classic" : [(500, 0), (150, 2), ,(800, 3)],
        # "pop" : [(600, 1), (2500, 4)] }
        # 각 장르별로 재생횟수와 인덱스를 튜플로 저장.
        gen[genres[i]] = gen.get(genres[i], []) + [(plays[i], i)]
        
    genSort = sorted(total.items(), key = lambda x: x[1], reverse=True)
    
    for (genre, totalPlay) in genSort:
        # 재생 횟수 내림차순, 인덱스 오름차순으로 정렬하기
        gen[genre] = sorted(gen[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in gen[genre][:2]]
        
    
    return answer