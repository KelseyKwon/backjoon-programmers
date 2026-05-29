from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    inInfo = defaultdict(int)
    parkingTime = defaultdict(int)
    
    def toInt(strs):
        h, m = map(int, strs.split(":"))
        return h * 60 + m
    
    for r in records:
        hour, carNum, isIn = r.split(" ")
        if isIn == 'OUT':
            parkingTime[carNum] += (toInt(hour) - inInfo[carNum])
            inInfo.pop(carNum)
        else:
            inInfo[carNum] = toInt(hour)
            
    outTime = toInt("23:59")
    for i in inInfo.keys():
        parkingTime[i] += outTime - inInfo[i]
    
    parked_time = dict(sorted(parkingTime.items()))
    
    basicTime, basicFee, plusTime, plusFee = fees
    
    for p in parked_time:
        if parked_time[p] > basicTime:
            finalFee = basicFee + (math.ceil((parked_time[p] - basicTime) / plusTime) * plusFee)
            answer.append(finalFee)
        else:
            answer.append(basicFee)
    
    return answer
            