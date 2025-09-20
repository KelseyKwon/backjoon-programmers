"""
일단 알파벳 딕셔너리 만들어
-> 그리고 key에 있는지 확인해 -> 없으면 딕셔너리에 추가.

딕셔너리의 가장 긴 문자열이 있는지. -> startswith로 확인?

msg
"""

def solution(msg):
    answer = []
    
    # chr은 뒤에를 아스키 코드로 바꿔주는 것. 
    # 'A' = 65 , 'a' = 97 -> 아스키 코드 값 확인하는법 : ord() 문자
    alphabet_dict = {chr(65+i): i+1 for i in range(26)}
    value = 27 # 새로운 단어를 추가할 인덱스 시작
    
    while msg:
        w = 0
        c = 1
        while msg[w:c] in alphabet_dict:
            c += 1
            if c > len(msg):
                break
        answer.append(alphabet_dict[msg[w:c-1]])
        
        alphabet_dict[msg[w:c]] = value
        value += 1
        msg = msg[c - 1:]
            

    return answer