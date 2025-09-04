"""
차량번호별로 -> 입차, 출차 짝짓고 그리고 출차 시간 - 입차 시간 구해.
case1 ) 입차, 출차 둘다 있음 
case2) 입차만 있음 -> 이 경우에는 23:59를 출차 시간으로 정하기

그리고 출차시간 - 입차시간 을 다 더해.

그리고 
case1) 만약에 fees[0] 넘지 않으면 : fees[1]
case2) fees[0]을 넘으면 ; ceil(총 시간 - fees[0] / fees[2]) * fees[3] + fees[1]

fees : 주차요금을 나타냄 -> [기본 시간, 기본 요금, 단위 시간, 단위 요금]
records : 입 / 출차 내역을 나타냄. -> ["시각 차량번호 IN/OUT"] 이렇게 나옴.

차량 번호가 작은 자동차부터 주차요금을 담은 배열 넘기기

일단 dict을 선언해 -> 

먼저 전체적으로 
1) 시간 계산해서 저장하기
2) 계산된 시간으로 주차요금 정산하기


"""
import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    
    base_time, base_fee, unit_time, unit_fee = fees
    # "차량 번호" : 입차 시간
    parking_status = {} # 현재 주차장에 있는 차량의 입차 시각을 저장하는 것
    
    total_time = defaultdict(int)
    
    for record in records:
        time_str, car_num, status = record.split()
        
        h, m = map(int, time_str.split(':'))
        minutes = h * 60 + m
        
        if status == 'IN':
            parking_status[car_num] = minutes
        else: #OUT일때
            in_time = parking_status.pop(car_num)
            parked_duration = minutes - in_time
            total_time[car_num] += parked_duration
    
    # 미출차 차량 처리 단계
    end_of_day_minutes = 23 * 60 + 59
    
    # parking_status에 남아있는 차량들은 미출차 기록 차량
    for car_num, in_time in parking_status.items():
        parked_duration = end_of_day_minutes - in_time
        total_time[car_num] += parked_duration
    
    answer = []
    
    sorted_car_nums = sorted(total_time.keys())
    
    for car_num in sorted_car_nums:
        if total_time[car_num] <= base_time:
            answer.append(base_fee)
        else:
            extra_time = total_time[car_num] - base_time
            extra_fee = math.ceil(extra_time / unit_time) * unit_fee
            final_fee = base_fee + extra_fee
            answer.append(final_fee)
    return answer