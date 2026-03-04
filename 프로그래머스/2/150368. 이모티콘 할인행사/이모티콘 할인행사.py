"""
플러스 가입자 늘리기! -> 판매액 늘리기!

users[n] -> 할인율 / 가격
emoticons

경계값 : 40 30 20 10 

i) 가입자 수를 늘려야돼!
싼거를 많이 할인해야 -> 가입자수가 늘어남!
일단 먼저 users를 구매금액 순으로 -> 같으면 할인율 순으로 해

완전 탐색으로 다 돌아봐
emoticons -> 내림차순으로 정렬
그리고 
"""

def solution(users, emoticons):
    all_discounts = []
    rates = [10, 20, 30, 40]
    
    # 전체 할인율 조합 생성기 -> 40, 30 / 40, 20 이런식으로
    def make_cases(current_case):
        if len(current_case) == len(emoticons):
            all_discounts.append(current_case[:])
            return
        
        for r in rates:
            current_case.append(r)
            make_cases(current_case)
            current_case.pop()
    
    make_cases([])
    
    answer = [0, 0]
    
    for case in all_discounts:
        # 일단 user별로 최소 할인율, 최소 금액 -> 어디까지 사야 이모티콘 플러스를 살지
        cur_plus, cur_buys = 0, 0
        for user_discount, user_amount in users:
            cur_amount = 0 # 이게 현재 금액
            for amount, discount in zip(emoticons, case):
                # if discount < user_discount:
                #     continue
                if discount >= user_discount:
                    cur_amount += amount * (100 - discount) // 100
            if cur_amount >= user_amount:
                cur_plus += 1
            else:
                cur_buys += cur_amount
        if cur_plus > answer[0]:
            answer = [cur_plus, int(cur_buys)]
            # answer[0], answer[1] = cur_plus, cur_buys
        elif cur_plus == answer[0]:
            # answer[1] = cur_buys
            answer[1] = max(answer[1], int(cur_buys))
        # else:
        #     continue
    
    return answer