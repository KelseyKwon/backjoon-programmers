"""
k : 부분 수열의 합
길이가 가장 짧은 수열을 찾기.
오름차순으로 정렬된 수열.

1부터 -> sequence의 길이 만큼

슬라이딩 윈도우! 3, 3-1+3, 5-2+4, 7-3+5 여기서 맞으면 -> 해당 인덱스를 반환해.

그럼 이걸 어떻게 구현하냐? 일단 sequence안에 k가 있으면 -> 해당 위치 반환
그 다음부터는 0:1까지 더하고, 

정답 : 투포인터 알고리즘. 정렬도니 데이터, 누적합 문제를 푸는데 특화되어 있음. 부분 수열의 합이 특정 값 'k' 에 도달하는 경우를 찾는 문제를 사용하면 됨.

합이 k와 일치하고 현재 부분 수열의 길이가 이전에 찾은 부분 수열의 최소 길이보다 짧은 경우 : 최소 길이와 정답을 업데이트.
"""

def solution(sequence, k):
    start, end = 0, 0
    current_sum = 0
    best_length = float('inf') # 최소값을 찾기 위해서 무한대로 초기화하기
    
    while end < len(sequence):
        current_sum += sequence[end]
        while current_sum >= k and start <= end: # 현재 구간의 합이 k 이상일 때 or start <= end일 때 왼쪽을 줄여서 합을 줄인다. 
            if current_sum == k:
                if end - start + 1 < best_length: # 구간 길이가 최단 길이보다 짧으면 갱신한다.
                    best_length = end - start + 1
                    answer = [start, end]
            current_sum -= sequence[start]
            start += 1
        end += 1
    
    return answer