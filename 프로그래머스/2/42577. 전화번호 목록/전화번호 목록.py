"""
한 번호가 다른 번호의 접두어인지 확인하는법

일단 배열을 순서대로 정렬하고

119 1195524421

뒤에 있는 원소가 직전에 있는 원소로 시작하면 false 반환
"""

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    prefix = phone_book[0].strip()
    
    if (len(phone_book) == 1):
        return True
    
    for i in range(1, len(phone_book)):
        if (phone_book[i].strip().startswith(prefix)):
            return False
        else:
            prefix = phone_book[i].strip()
    
    return True