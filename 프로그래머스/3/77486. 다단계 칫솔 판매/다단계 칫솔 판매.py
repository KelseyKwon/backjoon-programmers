from collections import defaultdict

def solution(enroll, referral, seller, amount):
    relation = defaultdict(str)
    money = defaultdict(int)

    for child, parent in zip(enroll, referral):
        relation[child] = parent

    for cur_seller, cur_amount in zip(seller, amount):
        total_amount = 100 * cur_amount          # 리스트가 아니라 수량 사용
        cur = cur_seller
        while cur != '-' and total_amount > 0:   # 전파 금액 0이면 종료
            commission = total_amount // 10
            money[cur] += total_amount - commission   # 변수명 수정
            cur = relation[cur]
            total_amount = commission

    return [money[name] for name in enroll]
