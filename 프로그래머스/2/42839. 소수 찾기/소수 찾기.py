import itertools

# 소수인지 아닌지 확인하는법
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    # 숫자를 자릿수로 쪼개기
    num_list = list(numbers)
    primes = set()

    #순열로 반복하기
    for r in range(1, len(num_list) + 1):
        for perm in itertools.permutations(num_list, r):
            # perm은 배열, 안의 각 요소들을 순서대로 꺼내서 
            # '' 구분자로 연결한다. 
            num = int(''.join(perm))
            if is_prime(num):
                primes.add(num)
    return len(primes)