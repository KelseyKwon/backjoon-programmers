
def solution(phone_book):
    phone_book.sort()
    prev = "-1"
    
    for phone in phone_book:
        if phone.startswith(prev):
            return False
        else:
            prev = phone
        
    return True