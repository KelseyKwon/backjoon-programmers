"""
1. list로 만들기
2. 순열로 모든 가능한 경우의 수 만들기
3. 2 이상인지 체크, 그리고 소수인지 체크
4. set에 담고 set의 길이를 반환.
"""
import itertools
def solution(numbers):
    answer = set()
    
    def isPrime(num):
        if num < 2:
            return False
        
        for i in range(2, num):
            if (num % i == 0):
                return False
        
        return True
    
    num_list = list(numbers)
    
    for i in range(1, len(numbers)+1):
        for temp in itertools.permutations(num_list, i):
            cur_num = int(''.join(temp))
            print(cur_num)
            if isPrime(cur_num):
                answer.add(cur_num)
    return len(answer)