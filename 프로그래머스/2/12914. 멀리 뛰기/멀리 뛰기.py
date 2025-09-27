def solution(n):
    answer = 0
    
    MOD = 1234567
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    fibb = [0] * (n+1)
    fibb[1] = 1
    fibb[2] = 2
    for i in range(3, n+1):
        fibb[i] = fibb[i-2] + fibb[i-1]
    
    return fibb[n] % MOD