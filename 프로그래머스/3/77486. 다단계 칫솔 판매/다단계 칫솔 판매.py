def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    total = {name: 0 for name in enroll}

    for i in range(len(seller)):
      money = 100 * amount[i]
      cur_seller = seller[i]
      # while(cur_seller != '-'):
      while (money > 0 and cur_seller != "-"):
        total[cur_seller] += money - money // 10
        money //= 10
        cur_seller = parent[cur_seller]

    return [total[name] for name in enroll]