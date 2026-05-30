"""

"""
import heapq

def solution(book_time):
    convert = []
    
    def converted(strs):
        h, m = map(int, strs.split(":"))
        return h * 60 + m
    
    for b in book_time:
        s, e = b
        s_time = converted(s)
        e_time = converted(e) + 10
        convert.append((s_time, e_time))
    convert.sort()
    room_info = []
        
    for i in range(len(convert)):
        if room_info and room_info[0] <= convert[i][0]:
            heapq.heappop(room_info)
        heapq.heappush(room_info, convert[i][1])
        
    return len(room_info)