"""
from collection
"""
from collections import defaultdict
import math

def solution(fees, records):
    info = defaultdict(int)
    is_in = defaultdict(int)
    
    def toInt(strs):
        h, m = map(int, strs.split(":"))
        return h * 60 + m
    
    for r in records:
        t, car_num, ins = r.split(" ")
        time = toInt(t)
        if ins == 'IN':
            is_in[car_num] = time
        else:
            info[car_num] += time - is_in[car_num]
            is_in.pop(car_num)
    
    for key, value in is_in.items():
        info[key] += toInt("23:59") - value
    
    infos = sorted(info.items(), key = lambda x:x[0])
    
    result = []
    basic_time, basic_fee, plus_time, plus_fee = fees
    for car, time in infos:
        if time > basic_time:
            cur_fee = basic_fee + math.ceil((time - basic_time) / plus_time) * plus_fee
            result.append(cur_fee)
        else:
            result.append(basic_fee)
    return result
            