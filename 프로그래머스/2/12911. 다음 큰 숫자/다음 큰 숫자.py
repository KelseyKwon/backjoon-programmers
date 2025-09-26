def solution(n):
    ones = bin(n).count('1')
    num = n + 1
    while bin(num).count('1') != ones:
        num += 1
    return num