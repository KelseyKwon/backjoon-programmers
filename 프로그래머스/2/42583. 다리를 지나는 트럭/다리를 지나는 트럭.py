"""
bridge_length대 올라갈 수 있다.
weight이하까지 무게를 견딜 수 있음.

"""
from collections import deque
def solution(bridge_length, weight, truck_weights):
    count = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    total_weight = 0
    
    while bridge:
        # 1. bridge 길이가 bridge_length 미만인지 확인 & bridge 의 현재 모든 weight + 현재 올릴려는 무게 <= weight인지 확인
        # 2. 이러면 추가
        # 3. 모든 분기마다 count += 1
        count += 1
        out = bridge.popleft()
        total_weight -= out
        
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.popleft()
                bridge.append(next_truck)
                total_weight += next_truck
            else:
                bridge.append(0)
    return count