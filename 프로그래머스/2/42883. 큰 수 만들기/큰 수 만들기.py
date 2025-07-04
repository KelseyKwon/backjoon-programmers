"""
start_index = 0
until ; start_index + k까지

그리고 선택하면 -> start_index가 선택한 index+1로 변환됨 (enumerate) -> k-=1

그리고 start_index + k까지
"""

def solution(number, k):
    stack = []
    
    for num in number :
        #스택의 꼭대기보다 비교 숫자가 크다면
        while stack and k > 0 and stack[-1] < num: 
            #스택의 맨 위 값을 제거하고 뽑는 개수 k도 -1
            stack.pop()
            k -= 1
        #현재 num 값은 무조건 스택에 추가
        stack.append(num)
    return "".join(stack[:len(number)-k])

        
        
    
    return answer