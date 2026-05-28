"""
최소 객실 -> 예약 현황을 바탕으로

일단 두번쨰 인자를 기준으로 정렬해. 
15:20 17:00 18:20 19:20 21:20

일단 첫번쨰 인자를 기준으로 정렬해. 
14:10 14:20 15:00 16:40 18:20

[] 에 append -> (1, 19:20) 이런식으로
"""
import heapq
def solution(book_time):
    
    def str_to_int(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
        
    formatted_book = []
    for start, end in book_time:
        _start = str_to_int(start)
        _end = str_to_int(end) + 10
        formatted_book.append((_start, _end))
    
    formatted_book.sort(key = lambda x:x[0])
    
    room_info = []
    for s, e in formatted_book:
        if room_info and room_info[0] <= s:
            heapq.heappop(room_info)
        heapq.heappush(room_info, e)
        
    return len(room_info)
        
    
    