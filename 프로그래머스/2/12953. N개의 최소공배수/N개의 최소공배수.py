"""
최소공배수를 구하는 법 : 다 나눠지는 소수가 있으면 -> 2, (1, 3, 4, 7) -> 168
1, 2, 3 -> 1이 나눠진느 소수야. -> 6

그럼 이렇게 나눠지는 것을 어떻게 아냐? 

두 수의 최소공배순느 최대공약수를 이용해 구할 수 있다.
최대공약수를 구하는 방법 : 유클리드 호제법. -> 나머지가 0이 될 떄의 b가 최대공약수

"""
# 유클리드 호제법
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소 공배수는 a * b를 최대공약수로 나눈것과 같다.
# 여기서 최대공약수는 유클리드 호제법을 이용해서 푼다. 
# 유클리드 호제법 : a -> b, b -> a % b로 치환
#여기서b가 1이 아닐때까지 계속. 
    
def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    arr.sort()
    temp = arr[0]
    for i in range(1, len(arr)):
        temp = lcm(temp, arr[i])
    return temp