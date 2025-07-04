
from collections import defaultdict

def solution(enroll, referral, seller, amount):
    # 1) child→parent 맵
    parent_map = {}
    for child, ref in zip(enroll, referral):
        parent_map[child] = ref

    # 2) 이익 누적용
    total_amount = defaultdict(int)

    # 3) 판매 기록 처리
    for s, cnt in zip(seller, amount):
        money = cnt * 100
        cur = s
        while cur != '-' and money > 0:
            commission = money // 10              # 부모에게 보낼 10% (버림)
            total_amount[cur] += money - commission  # 내 몫
            cur = parent_map[cur]                 # 부모로 이동
            money = commission                    # 남은 금액을 부모가 분배
        # 최상위(센터)에게도 남은 금액이 있다면 추가
        if cur == '-' and money > 0:
            total_amount[cur] += money

    # 4) enroll 순서대로 결과 반환
    return [ total_amount[name] for name in enroll ]
