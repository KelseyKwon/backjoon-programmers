"""
min arrayA, arrayB 의 약수들이 후보 -> 배열에 담아놨다가
크기 순서대로 탐색.
"""
import math

def solution(arrayA, arrayB):
    gcdA = arrayA[0]
    for x in arrayA[1:]:
        gcdA = math.gcd(gcdA, x)
    
    gcdB = arrayB[0]
    for x in arrayB[1:]:
        gcdB = math.gcd(gcdB, x)
    
    # 만약에 둘다 1이면 -> 0 return
    # 같은거 check
    if (gcdA == gcdB):
        return 0
    
    if (gcdA > gcdB):
        if all(b % gcdA != 0 for b in arrayB):
            return gcdA
    else:
        if all(a % gcdB != 0 for a in arrayA):
            return gcdB
    
    return 0
    
    
