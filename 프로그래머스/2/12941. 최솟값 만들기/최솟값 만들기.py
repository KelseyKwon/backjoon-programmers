"""
각 배열의 값끼리 더해서 가장 최소가 되는 값을 내놓기.
그러면 각 배열을 먼저 정렬해  -> 
처음배열은 오름차순, 뒤의 배열은 내림차순으로
[1, 2, 4] [5, 4, 4] -> 5 + 8 + 16 -> 29
[1, 2] [4, 3] -> 4 + 6

"""

def solution(A,B):
    answer = 0
    
    n = len(A)

    A.sort()
    B.sort(reverse = True)
    
    print(A)
    print(B)
    
    for i in range(n):
        answer += (A[i] * B[i])
        print(answer)

    return answer