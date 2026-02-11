"""
흔적을 최소화!

물건을 훔지는 조건
-> 훔치면 info[i][0] (i가 물건, 0 / 1이 A or B 도둑)
-> 1 이상 3 이하

A 도둑 : n , B 도둑 : m

A 도둑의 흔적을 최소화하라!

즉, len(info) <= max(n, m) -> 크면 -1 리턴!
     A. B.   A. B.  A.  B
   [[1, 2], [2, 3], [2, 1]]
물건    1      2       3

3, 2, 1

다 더해 -> 6 -> 6 > m -> 5 > m -> 5 - 3 + 2

dp[] = b의 흔적의 최대값...
dp[] = dp[]

즉, A의 흔적과 B의 흔적을 기준으로 딕셔너리에 저장한다. 
     
"""

def solution(info, n, m):
    # prev_state[A] = B
    prev_state = {0: 0}

    # 각 물건에 대해 DP 갱신
    for x, y in info:
        next_state = {}

        for A, B in prev_state.items():
            # A가 훔치는 경우
            if A + x < n:
                if (A + x) not in next_state or next_state[A + x] > B:
                    next_state[A + x] = B

            # B가 훔치는 경우
            if B + y < m:
                if A not in next_state or next_state[A] > B + y:
                    next_state[A] = B + y

        # 이번 물건 처리 후 가능한 상태가 없다면 실패
        if not next_state:
            return -1

        # 다음 단계로 상태 갱신
        prev_state = next_state

    # 모든 물건을 처리한 후, A 흔적의 최소값 반환
    return min(prev_state.keys())
