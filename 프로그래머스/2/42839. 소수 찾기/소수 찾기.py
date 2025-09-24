"""
일단 1개 만드는 상황 -> len(numbers)까지 만드는 상황

for i in range(len)
if 소수 : answer += 1

"""
from itertools import permutations
import math

def solution(numbers):
    answer = 0
    nums = set()
    # 소수 인지 확인하는법
    def isPrime(n):
        if n < 2:
            return False
        # 약수는 항상 n^1/2 이하에서 발견된다. 
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    # permutations는 iterable 객체에서 r개를 뽑아 모든 순열을 생성한다.
    for i in range(1, len(numbers) + 1):
        # numbers도 일종의 배열이다.
        for p in permutations(numbers, i):
            temp = int("".join(p))
            if temp not in nums:
                nums.add(temp)
                if isPrime(temp):
                    answer += 1
    
    return answer