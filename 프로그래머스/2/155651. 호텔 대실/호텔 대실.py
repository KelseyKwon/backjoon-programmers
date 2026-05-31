"""

"""
import heapq

def solution(book_time):
    converted = []
    
    def toInt(strs):
        h, m = map(int, strs.split(":"))
        return h * 60 + m
    
    for i, o in book_time:
        converted.append((toInt(i), toInt(o) + 10))
    
    converted.sort(key = lambda x : x[0])
    rooms = [] 
    for i, o in converted:
        if rooms and rooms[0] <= i:
            heapq.heappop(rooms)
        heapq.heappush(rooms, o)
    
    return len(rooms)
        