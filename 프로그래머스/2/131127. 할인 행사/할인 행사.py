from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    
    product_count = sum(number)
    end_start_index = len(discount) - product_count + 1
    
    for i in range(end_start_index):
        info = defaultdict(int)
        for product, count in zip(want, number):
            info[product] = count
        temp_discount = discount[i:i+product_count]

        # 임시 저장배열을 돌면서 감소시키기
        for k in temp_discount:
            if k in list(info.keys()):
                info[k] -= 1
        is_zero = True   
        for k, v in info.items():
            if v != 0:
                is_zero = False
                break
        if (is_zero):
            answer += 1
    return answer