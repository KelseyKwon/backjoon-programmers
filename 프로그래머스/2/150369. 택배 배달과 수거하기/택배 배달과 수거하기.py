"""
관점의 전환이 필요하다
거꾸로 부터 도는 것은 괜찮으나, 각 배달의 개수에서 cap을 빼서, 0보다 크면 계속 거기에 가야 하는 거고, 아니면 그 전으로 되돌아가도 돼!
"""

def solution(cap, n, deliveries, pickups):
    
    delivery = 0
    pickup = 0
    answer = 0
    
    for i in range(len(deliveries) - 1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            
            answer += (i + 1) * 2
    return answer
            
        